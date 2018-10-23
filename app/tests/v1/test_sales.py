import unittest
import requests
import pytest
from app import create_app
from flask import json

class TestSales(unittest.TestCase):
	def setUp(self):
		self.client=create_app("config").test_client()
		self.client.testing = True
		self.sale={
				 "attendant": "kim Jun un",
		"price": 23544,
		"product_id": "f17a5648-d6f2-11e8-abec-2cd05a4568e3",
		"product_name": "Jordans",
		"quantity": 16,
		"sale_id": 2,
		"total_sale": 2340000
			}
	def test_get(self):
		response = self.client.get("/api/v1/sales",
								headers={'content_type': 'application/json'})
		self.assertEqual(response.status_code,200)
	def login(self):
		login_details = self.client.post("http://127.0.0.1:5000/api/v1/users/login",
			data=json.dumps(dict(email="jenna@gmail.com",password="1234567890")),
			content_type='application/json')
		return json.loads(login_details.data.decode())["access_token"]
	def test_post(self):
		response=self.client.post('http://127.0.0.1:5000/api/v1/sales',
								data= json.dumps(self.sale),
							   headers=dict(Authorization="Bearer " + self.login()),
							  content_type='application/json')
		res = json.loads(response.data.decode())
		# self.assertTrue(res["message"] == "product successfully added")
		self.assertEqual(response.status_code,201)

class Test_Get_sale_id(unittest.TestCase):
	def setUp(self):
		self.client=create_app("config").test_client()
		self.client.testing = True
		self.sale={"attendant": "kim Jun un",
				"price": 23544,
				"product_id": "197b7a5a-d2b1-11e8-b840-53b0b2c94072",
				"product_name": "Jordans",
				"quantity": 16,
				"sale_id": 37,
				"total_sale": 2340000}
	def test_get(self):
		sale = {"attendant": "kim Jun un",
				"price": 23544,
				"product_id": "197b7a5a-d2b1-11e8-b840-53b0b2c94072",
				"product_name": "Jordans",
				"quantity": 16,
				"sale_id": 37,
				"total_sale": 2340000}
		response = self.client.get("http://127.0.0.1:5000/api/v1/sales/37",
								headers={'content_type': 'application/json'})
		self.assertEqual(response.status_code,200)
