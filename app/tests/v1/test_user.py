import unittest
import requests
import pytest
from app import create_app
from flask import json


class UserTestCase(unittest.TestCase):
	def setUp(self):
		self.app=create_app("testing")
		self.client=self.app.test_client()
		self.register_user={ "email": "test@gmail.com", "password":"1234567890"}
		self.register_user_empty_email = { "email": "", "password":"1234567890"}
		self.login_user = { "email": "higi@gmail.com", "password":"1234567890" }
		self.login_user_empty_email= { "email": "", "password":"1234567890" }
		self.login_user_empty_password= { "email": "higi@gmail.com", "password":""}
	def test_registration(self):
		response = self.client.post('http://127.0.0.1:5000/api/v1/users/registration',data=json.dumps(dict(
				email='higi@gmail.com',password='1234567890')),content_type='application/json')
		data = json.loads(response.data.decode())
		self.assertTrue(data['status'] == 'ok')
		self.assertTrue(data['message'] == 'User was created succesfully')
		self.assertTrue(response.content_type == 'application/json')
		self.assertEqual(response.status_code, 201)


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
	def test_sign_up_empty_email(self):
	 	res = self.client.post("http://127.0.0.1:5000/api/v1/users/registration", data=json.dumps(self.register_user_empty_email),
								 content_type='application/json')
	 	resp_data = json.loads(res.data.decode())
	 	self.assertEqual(res.status_code, 500)
	def test_login_empty_email(self):
		res_login = self.client.post("http://127.0.0.1:5000/api/v1/users/login", data=json.dumps(self.login_user_empty_email),
									   content_type='application/json')
		resp_data = json.loads(res_login.data.decode())
		self.assertEqual(res_login.status_code, 400)

	def test_login_empty_password(self):
		res_login = self.client.post("http://127.0.0.1:5000/api/v1/users/login", data=json.dumps(self.login_user_empty_password),
									   content_type='application/json')
		resp_data = json.loads(res_login.data.decode())
		self.assertEqual(res_login.status_code, 400)
