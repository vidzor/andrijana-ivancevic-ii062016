
from MyUser import MyUser, MyEncoder
import os
import json
import copy
import re

class MyUserRepo():

	def __init__(self):
		self.users = []
		self.encoder = MyEncoder()
		self.db_filename = 'mydatabase.json'
		self.load()

	def get_user(self, user):
		user_id = 0
		if isinstance( user, MyUser ):
			user_id = user.id
		elif isinstance( user, int ):
			user_id = user
		else:
			return None

		for user in self.users:
			if user.id == user_id:
				return user

	def get_users(self):
		self.sort_users_by_date()
		return self.users
	
	def search_users(self, search_term):
		found_users = []
		for user in self.users:
			if re.findall( r''+search_term, user.name, re.IGNORECASE ):
				found_users.append(user)
		return found_users
	
	def sort_users_by_date(self):
		keyfun = lambda user: user.creation_datetime
		self.users.sort( key=keyfun, reverse=True )

	def generate_new_id(self):
		new_id = len(self.users)+1
		while True:
			found_it = False
			for user in self.users:
				if new_id == user.id:
					found_it = True
					new_id += 1
			if not found_it: break
		return new_id


	def add_user(self, new_user):
		new_id = self.generate_new_id()
		new_user.id = new_id
		self.users.append(new_user)
		self.persist()

	def remove_user(self, user2remove):
		for user in self.users:
			if user.id == user2remove.id:
				self.users.remove(user2remove)
				self.persist()
				return 'SUCCESS'
		return 'FAIL'
	
	def persist(self):
		users = copy.deepcopy(self.users)
		data = self.encoder.encode( users )
		db = open( self.db_filename, 'w' )
		db.write(data)
		db.close()
		
	def clear_all_users(self):
		self.users = []
		self.persist()
	
	def load(self):
		if os.path.exists(self.db_filename):
			db = open( self.db_filename, 'r' )
			data = db.read()
			db.close()
			
			users_dicts = json.loads(data)
			self.users = []
			
			for user_dict in users_dicts:
				user = MyUser()
				user.deserialize(user_dict)
				self.users.append(user)
			
		else:
			print(' Database does not exist ')