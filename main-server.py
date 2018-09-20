
from flask import Flask, render_template, request, Response
app = Flask(__name__)

import json

from MyUser import MyUser
from MyUsersRepo import MyUserRepo

repo = MyUserRepo()

@app.after_request
def add_header(r):
	# Add headers to both force latest IE rendering engine or Chrome Frame,
	# and also to cache the rendered page for 10 minutes.
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
	r.headers['Cache-Control'] = 'public, max-age=0'
	return r

@app.route("/", methods=['GET'])
def load_index():
	return render_template('index.html')

@app.route("/users/getall", methods=['GET'])
def get_all_users():
	users = repo.get_users()
	return render_template( 'listusers.html', users=users )

@app.route("/users/search/<search_term>", methods=['GET'])
def search_users(search_term):
	users = repo.search_users(search_term)
	return render_template('listusers.html', users=users)

@app.route("/users/add", methods=['POST'])
def add_user():
	user_dict = request.get_json()
	# user_dict = json.loads( user_json )
	
	new_user = MyUser()
	new_user.deserialize( user_dict )
	repo.add_user( new_user )
	
	return Response('DONE', status=200)

@app.route("/users/remove/<user_id>", methods=['DELETE'])
def remove_user(user_id):
	user2remove = repo.get_user( int(user_id) )
	repo.remove_user( user2remove )
	return Response('DONE', status=200)


if __name__ == "__main__":
	
	# from time import sleep
	#
	# user1 = MyUser()
	# user1.quickset_params( name='John',  age=23, height=180 ),
	# repo.add_user(user1)
	# sleep(1)
	#
	# user2 = MyUser()
	# user2.quickset_params( name='Smith', age=13, height=172 ),
	# repo.add_user(user2)
	# sleep(1)
	#
	# user3 = MyUser()
	# user3.quickset_params( name='Jane',  age=45, height=170 )
	# repo.add_user(user3)
	
	app.run(host='0.0.0.0')