
from json import JSONEncoder
import datetime


class MyEncoder(JSONEncoder):
	def default(self, o):
		d = o.__dict__
		d['_creation_datetime'] = o.get_creation_datetime_str()
		return o.__dict__

class MyUser:

	def __init__(self):
		self._id = 0
		self._name = ''
		self._age = 0
		self._height = 0
		self._datetime_format = "%Y-%m-%d %H:%M:%S"
		self._creation_datetime = datetime.datetime.now()
	
	# GETers and SETers:

	@property
	def id(self): return self._id
	@id.setter
	def id(self, value): self._id = value

	@property
	def name(self): return self._name
	@name.setter
	def name(self, value): self._name = value

	@property
	def age(self): return self._age
	@age.setter
	def age(self, value): self._age = value

	@property
	def height(self): return self._height
	@height.setter
	def height(self, value): self._height = value
	
	@property
	def datetime_format(self): return self._datetime_format
	@datetime_format.setter
	def datetime_format(self, value): self._datetime_format = value
	
	def get_creation_datetime_obj(self): return self._creation_datetime
	def get_creation_datetime_str(self): return self._creation_datetime.strftime( self._datetime_format )
	@property
	def creation_datetime(self): return self.get_creation_datetime_obj()
	@creation_datetime.setter
	def creation_datetime(self, value):
		if type(value) == str:
			self._creation_datetime = datetime.datetime.strptime( value, self._datetime_format )
		elif type(value) == datetime.datetime:
			self._creation_datetime = value
	
	def quickset_params(self, name, age, height):
		self.name = name
		self.age = age
		self.height = height
	
	def deserialize(self, user_dict):
		
		user_dict_ = {}
		for key in user_dict.keys():
			key_ = key
			if key[0] != '_': key_ = f'_{key}'
			user_dict_[key_] = user_dict[key]
		
		self.id = user_dict_['_id']
		self.name = user_dict_['_name']
		self.age = user_dict_['_age']
		self.height = user_dict_['_height']
		if user_dict_['_creation_datetime']:
			self.creation_datetime = user_dict_['_creation_datetime']

