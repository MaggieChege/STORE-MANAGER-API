from flask_restful import Resource, Api
from flask import request, jsonify, json, make_response
from app.api.v1.models import Users as U , users
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
class UserRegistration(Resource):
	def post(self):
		data = request.get_json()
		username = data['username']
		email = data['email']
		raw_password = data['password']
		role = data['role']

		password = U.generate_hash(raw_password)
		user = U(username,email,password,role).create_user()
		users.append(user)
		return make_response(jsonify({
            "Users" : users
}),201)

class UserLogin(Resource):
	def post(self):
		data = request.get_json()
		email = request.get_json('email')
		password=request.get_json('password')
		if not email:
			return {"message","email cannot be empty"}
		if not password:
			return {"message","password cannot be empty"}

		current_user = U.find_by_email(email)
		# check if user exists
		if current_user == 0:
			return {"message": "email doesnt exist"},400

		if U.verify_hash(password,email) == True:
			access_token = create_access_token(identity = email)
			refresh_token = create_refresh_token(identity = email)

			return make_response(jsonify({
			'message':"User has successfully Logged in",
			"status": "ok",
			"access_token":access_token,
			"refresh_token": refresh_token
			}),200)

		else:
			return make_response(jsonify({"message": "Wrong Username or password"}),400)
