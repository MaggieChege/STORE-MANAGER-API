from flask import make_response, jsonify
from passlib.hash import pbkdf2_sha256 as sha256

users =[]


class Users:
    """ Initialize the user """
    def __init__(self, username, email, password, role):
        self.userid = len(users)+1
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def create_user(self):
        user = {
            "userid": self.userid,
            "username" : self.username,
            "email" : self.email,
            "password" : self.password,
            "role" : self.role
        }
        return user

    def generate_hash(raw_password):
    	return sha256.hash(raw_password)

    @staticmethod
    def find_by_email(email):
        for x in users :
            listOfKeys = [key  for (key, value) in x.items() if value == email]
            if listOfKeys:
                return 1

            return 0
    @staticmethod
    def verify_hash(password,email):
    	for x in users :
    		listOfKeys = [key  for (key, value) in x.items() if value == email]
    		if listOfKeys:
    			result = list(filter(lambda person: person['email'] == email, users))
    			return sha256.verify(password,  result[0]['password'] )
