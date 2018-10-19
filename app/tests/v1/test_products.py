import unittest
import requests
import pytest
from app import create_app
from flask import json

class TestProducts(unittest.TestCase):
	def setUp(self):
		self.app=create_app("config").test_client()
		self.app.testing = True
		self.products={"product_id":1,
                       "product_name":"Bread",
                       "quantity":2,
                       "price":20}
	def test_get(self):
		response = self.app.get("/api/v1/products",
                                headers={'content_type': 'application/json'})
		self.assertEqual(response.status_code,200)

	def test_post(self):
		product ={"price": 3500,"product_id": 47,"product_name": "jordans","quantity": 20}
		response=self.app.post('http://127.0.0.1:5000/api/v1/products',
                               data=json.dumps(product),
                              content_type='application/json')
		self.assertEqual(response.status_code,201)



class Test_Get_product_id(unittest.TestCase):
	def setUp(self):
		self.app=create_app("config").test_client()
		self.app.testing = True
		product={"product_id":1,
                       "product_name":"Bread",
                       "quantity":2,
                       "price":20 }
	def test_get(self):
		product={"product_id":1,
                       "product_name":"Bread",
                       "quantity":2,
                       "price":20}
		response = self.app.get("http://127.0.0.1:5000/api/v1/products/3",
                                headers={'content_type': 'application/json'})
		self.assertEqual(response.status_code,200)



