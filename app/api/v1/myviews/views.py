from flask_restful import Resource, Api
from flask import request, jsonify, json, make_response
import uuid
import re
import random
from app.api.v1.models import Users as U ,users
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

products = []
sales =[]
class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        email = data['email']
        raw_password = data['password']
        role = data['role']
        if not email or "":
            return {"message","email cannot be empty"}
        if not re.match(r"[^@]+@[^@]+\.[^@]+",email):
            return {"message": "Enter correct email format"}
        if not raw_password:
            return {"message","password cannot be empty"}
        if len(raw_password) < 6:
            return {"message","password is too short"}
        if not role or  role == "":
            return 404
        # check_email = email(find_by_email)

        password = U.generate_hash(raw_password)
        current_user = U.find_by_email(email)
        if current_user == 1:
            return {'message': 'email already exist'},400
        try:
            user = U(username,email,password,role).create_user()
            access_token = create_access_token(identity = email)
            refresh_token = create_refresh_token(identity = email)
            users.append(user)

            return {

            "Users" : users,
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
        email = request.get_json('email')
        password=request.get_json('password')
        if not email or email == "":
            return {"message","email cannot be empty"}
        if not password or password == "":
            return {"message","password cannot be empty"}
            
        # if email == 'jane@gmail.com' and password == '1234567890':
        if U.verify_hash(password,email) == True:
            access_token = create_access_token(identity = email)
            refresh_token = create_refresh_token(identity = email)

            return stringify({
                'message': 'User was logged in succesfully',
                'status': 'ok',
                'access_token': access_token,
                'refresh_token': refresh_token
                }), 200
            

               
        else:
            return {'message': 'Wrong credentials'},400

class Products(Resource):
	def get(self):
		return jsonify(products)
	@jwt_required
	def post(self):
		
		product_id = len(products)
		product_name = request.json.get('product_name')
		price = request.json.get('price')
		quantity = request.json.get('quantity')
		if not product_name or product_name == "":
			return 404
		else:
			product = { 
			"product_id": product_id,
			"product_name" : product_name,
			"price" : price,
			"quantity": quantity
			}

			products.append(product)
			return make_response(jsonify({'product':products}),201)

class Sales(Resource):
	def get(self):
		return jsonify(sales)

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
		else:
			sale = { 
			"sale_id": sale_id,
			"product_id": product_id,
			"product_name" : product_name,
			"price" : price,
			"attendant" : attendant,
			"total_sale" :total_sale,
			"quantity": quantity
			}

		sales.append(sale)
		return make_response(jsonify({'sale':sales}),201)
	
class Get_sale_id(Resource):
	def get(self,sale_id):
		sal = [sale for sale in sales if sale['sale_id'] == sale_id] or None
		if sal:
			return make_response(jsonify({'sale':sal[0]}),200)
		else:
			return jsonify({'message': "specific product not found"})
			

		return 404


	
class Get_product_id(Resource):
	# @jwt_required
	def get(self,product_id):
		pro = [product for product in products if product['product_id'] == product_id] or None
		if pro:
			return jsonify({'product':pro[0]})
		else:
			return jsonify({'message': "specific product not found"})
			

		return 404


