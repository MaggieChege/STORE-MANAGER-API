from flask_restful import Resource, Api
from flask import request, jsonify, json, make_response
import uuid
import random
# blue = Blueprint()

products = []
sales =[]


class Products(Resource):
	def get(self):
		return jsonify(products)

	def post(self):
		
		product_id = random.randint(1,100)
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
	def get(self,product_id):
		pro = [product for product in products if product['product_id'] == product_id] or None
		if pro:
			return jsonify({'product':pro[0]})
		else:
			return jsonify({'message': "specific product not found"})
			

		return 404


