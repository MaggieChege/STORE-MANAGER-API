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
		self.products={"price": 20,
            "product_id": 1,
            "product_name": "jordans",
            "quantity": 23}
    
		
	def test_get(self):
		response = self.client.get("/api/v1/products",
                                headers={'content_type': 'application/json'})
		self.assertEqual(response.status_code,200)
	def login(self):
		login_details = self.client.post("http://127.0.0.1:5000/api/v1/users/login",
			data=json.dumps(dict(email="jenna@gmail.com",password="1234567890")),
			content_type='application/json')
		return json.loads(login_details.data.decode())["access_token"]
	def test_post(self):
		response=self.client.post('http://127.0.0.1:5000/api/v1/products',
								data= json.dumps(self.products),
                               headers=dict(Authorization="Bearer " + self.login()),
                              content_type='application/json')
		res = json.loads(response.data.decode())
		# self.assertTrue(res["message"] == "product successfully added")
		self.assertEqual(response.status_code,201)



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



