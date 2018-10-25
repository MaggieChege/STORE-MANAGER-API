import unittest
import sys
import requests
import pytest
from app import create_app
from flask import json

class TestProducts(unittest.TestCase):

	def setUp(self):
		self.client=create_app("config").test_client()
		self.client.testing = True
		self.products={"price": 20,"product_id": 1,"product_name": "jordans","quantity": 23}
		self.empty_price={"price": "","product_id": 1,"product_name": "jordans","quantity": 23}
		self.empty_products={"price": 20,"product_id": 1,"product_name": "","quantity": 23}
		self.empty_quantity={"price": 20,"product_id": 1,"product_name": "","quantity": ""}
	def test_get(self):
		response = self.client.get("/api/v1/products",
                                headers={'content_type': 'application/json'})
		self.assertEqual(response.status_code,200)
	def test_login(self):
		response = self.client.post('http://127.0.0.1:5000/api/v1/users/login',data=json.dumps(dict(
                email='higi@gmail.com',password='1234567890')),content_type='application/json')
		data = json.loads(response.data.decode())
		return data
		self.assertTrue(data['status'] == 'ok')
		self.assertTrue(data['message'] == 'You logged in successfully')
		self.assertTrue(data['access_token'])
		self.assertTrue(response.content_type == 'application/json')
		self.assertEqual(response.status_code, 200)

	def test_post(self):
		response=self.client.post('http://127.0.0.1:5000/api/v1/products',
								data= json.dumps(self.products),
								content_type = 'application/json')
		resp_data = json.loads(response.data.decode())
		return resp_data
		self.assertTrue(resp_data['message'] == 'product created successfully')
		self.assertEqual(response.status_code, 201)
	def test_empty_name_product(self):
		response = self.client.post("http://127.0.0.1:5000/api/v1/products",
                                    data = json.dumps(self.empty_products),
                                    content_type = 'application/json')
		resp_data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 500)
	def test_empty_price_product(self):
		response = self.client.post("http://127.0.0.1:5000/api/v1/products",
                                    data = json.dumps(self.empty_price),
                                    content_type = 'application/json') 
		resp_data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 500)
	def test_empty_quantity_product(self):
		response = self.client.post("http://127.0.0.1:5000/api/v1/products",
                                    data = json.dumps(self.empty_quantity),
                                    content_type='application/json')
		resp_data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 500)

class Test_Get_product_id(unittest.TestCase):
	def setUp(self):
		self.client=create_app("config").test_client()
		self.client.testing = True
		product={"product_id":1,
                       "product_name":"Bread",
                       "quantity":2,
                       "price":20 }
	def test_get(self):
		product={"product_id":1,
                       "product_name":"Bread",
                       "quantity":2,
                       "price":20}
		response = self.client.get("http://127.0.0.1:5000/api/v1/products/3",
                                headers={'content_type': 'application/json'})
		self.assertEqual(response.status_code,200)



