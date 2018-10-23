
from flask import make_response, jsonify
from passlib.hash import pbkdf2_sha256 as sha256

users =[{
            "email": "jenna@gmail.com",
            "password": "$pbkdf2-sha256$29000$g7B27n0PwViL0RpDKCUE4A$3LZ17MobpNzcB6dpyY/bFceHi3Vlu2qe1Z.HXwXsUHU",
            "role": "admin",
            "userid": 1,
            "username": "jane"
        }]
products =[]
sales =[]

class Users:
    def create_user(email,password):
        userid = len(users)+ 1
        # "username" : username,,"role" :role 
        user = {"email" : email,"password" : password}
        users.append(user)
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
        user = next((item for item in users if item["email"] == email), False)
        if user == False:
             return False
        return sha256.verify(password, user['password'] )
class Product():  
    @staticmethod
    def create_product(product_name, price, quantity):
        product_id= len(products) +1
        product = { "product_id":product_id,"product_name" : product_name,"price" :price,"quantity": quantity}
        products.append(product)
        return products

    @staticmethod
    def get_product():
        return products

    @staticmethod
    def get_one_product(product_id):
        pro = [product for product in products if product['product_id'] == product_id] or None
        if pro:
            return jsonify({'product':pro[0]})
        else:
            return jsonify({'message': "specific product not found"})
            

        return 404

class Sale():
    @staticmethod
    def get_sales():
        return sales
    @staticmethod
    def create_sale(product_id,product_name,price,attendant,total_sale,quantity):
        sale_id= len(sales) +1
        sale ={"sale_id": sale_id,"product_id": product_id,"product_name" : product_name,"price" : price,"attendant" : attendant,"total_sale" :total_sale,"quantity": quantity}
        sales.append(sale)
        return sales

