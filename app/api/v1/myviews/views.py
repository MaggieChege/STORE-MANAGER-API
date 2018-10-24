from flask_restful import Resource, Api,reqparse
from flask import request, jsonify, json, make_response
import uuid
import re
import random
from app.api.v1.models import Users,users
from app.api.v1.models import Product,products
from app.api.v1.models import Sale,sales
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

class UserRegistration(Resource):
	def post(self):
		data = request.get_json()
		# username = data['username']
		email = data['email']
		raw_password = data['password']
		# role = data['role']
		if not email or email =="":
			return {"message","email cannot be empty"}
		if not re.match(r"[^@]+@[^@]+\.[^@]+",email):
			return {"message": "Enter correct email format"}
					# generate hash value for rawpassword
		password = Users.generate_hash(raw_password)
		current_user = Users.find_by_email(email)
		user_info = {"email":email,"password":password}
		# user_info.create_user(user_info)
		if current_user == 1:
			return {'message': 'email already exist'},400
		try:
			user = Users(email,password).create_user()
			access_token = create_access_token(identity = email)
			refresh_token = create_refresh_token(identity = email)
			users.append(user)

			return {

			"Users" : user,
				'message': 'User was created succesfully',
				'status': 'ok',
				'access_token': access_token,
				'refresh_token': refresh_token
				}, 201

		except Exception as e:
			print(e)

class UserLogin(Resource):

	def post(self):
		data = request.get_json()
		email = data['email']
		password = data['password']
		if not email or email =="":
			return {'message': 'email can not be empty'},400
		if not password or email == "":
			return {'message': 'password cannot be empty'},400

  # check if user email exists avoid duplication 
		current_user = Users.find_by_email(email)
		if current_user == False:
			return {'message': 'email does not  exist'},400


		
		# verify password matches with hash value
		if Users.verify_hash(password,email) == True:
			access_token = create_access_token(identity = email)
			refresh_token = create_refresh_token(identity = email)

			return {
				'message': 'User was logged in succesfully',
				'status': 'ok',
				'access_token': access_token,
				'refresh_token': refresh_token
				}, 200
			

			   
		else:
			return {'message': 'Wrong credentials'},400
			   
		# else:
		#     return {'message': 'Wrong credentials'},400

class Products(Resource):
	def get(self):
		products = Product.get_product()
		return jsonify(products)
	@jwt_required
	def post(self):
		
		# product_id = len(products)
		product_name = request.json.get('product_name')
		price = request.json.get('price')
		quantity = request.json.get('quantity')
		if not product_name or product_name == "":
			return 404
		if not price or price == "":
			return 404       
		if not quantity or quantity == "":
			return 404
		try:
			product = Product(product_id,product_name, price, quantity).create_product()
			return make_response(jsonify({'product':product}),201)
		except Exception:
		    print(Exception)
		    return {"message":"Something went wrong"},500
class Get_product_id(Resource):
	
	def get(self,product_id):
		pro = [product for product in products if product['product_id'] == product_id] or None
		if pro:
			return jsonify({'product':pro[0]})
		else:
			return jsonify({'message': "specific product not found"})
			


class Sales(Resource):
	def get(self):
		sales = Sale.get_sales()
		return jsonify(sales)
	@jwt_required
	def post(self):
		product_id = uuid.uuid1()
		sale_id = random.randint(1,100)
		product_name = request.json.get('product_name')
		price = request.json.get('price')
		total_sale= request.json.get('total_sale')
		attendant = request.json.get("attendant")
		quantity = request.json.get('quantity')
		if not product_name or product_name == "":
			return 404
		sale = Sale(product_id,product_name,price,attendant,total_sale,quantity).create_sale()
		return make_response(jsonify({'sale':sale}),201)
	
class Get_sale_id(Resource):
	def get(self,sale_id):
		sal = [sale for sale in sales if sale['sale_id'] == sale_id] or None
		if sal:
			return make_response(jsonify({'sale':sal[0]}),200)
		else:
			return jsonify({'message': "specific product not found"})
			

		return 404


	

