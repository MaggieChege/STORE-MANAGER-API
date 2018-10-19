import unittest
import requests
import pytest
from app import create_app
from flask import json

class TestSales(unittest.TestCase):
	def setUp(self):
		self.app=create_app("config").test_client()
		self.app.testing = True
		self.sale={
                "attendant": "kim Jun un",
                "price": 23544,
                "product_id": "197b7a5a-d2b1-11e8-b840-53b0b2c94072",
                "product_name": "Jordans",
                "quantity": 16,
                "sale_id": 37,
                "total_sale": 2340000
            }

	def test_get(self):
		response = self.app.get("/api/v1/sales",
                                headers={'content_type': 'application/json'})
		self.assertEqual(response.status_code,200)
	def test_post(self):
		sale = {"attendant": "kim Jun un",
                "price": 23544,
                "product_id": "197b7a5a-d2b1-11e8-b840-53b0b2c94072",
                "product_name": "Jordans",
                "quantity": 16,
                "sale_id": 37,
                "total_sale": 2340000}
		response=self.app.post('http://127.0.0.1:5000/api/v1/sales',data=json.dumps(sale),content_type = 'application/json')
		self.assertEqual(response.status_code,201)

class Test_Get_sale_id(unittest.TestCase):
	def setUp(self):
		self.app=create_app("config").test_client()
		self.app.testing = True
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
		response = self.app.get("http://127.0.0.1:5000/api/v1/sales/37",
                                headers={'content_type': 'application/json'})
		self.assertEqual(response.status_code,200)
