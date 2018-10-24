
from flask import make_response, jsonify
from passlib.hash import pbkdf2_sha256 as sha256

users =[]
products =[]
sales =[]

class Users:
    def __init__(self,email,password):
        self.email=email
        self.password=password
    def create_user(self):
        user = {"email":self.email,"password":self.password}
        userid = len(users)+ 1
        # "username" : username,,"role" :role 
        
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
    def __init__(self,product_id,product_name,price,quantity):
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        self.quantity=quantity

    def create_product(self):
        product_id =len(products)+1
        # "product_id":self.product_id,
        product = {"product_id":self.product_id,"product_name":self.product_name,"price":self.price,"quantity":self.quantity}
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
    def __init__(self,sale_id,product_id,product_name,price,attendant,total_sale,quantity):
        self.sale_id=(sale_id)
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        self.attendant=attendant
        self.total_sale=total_sale
        self.quantity=quantity
    @staticmethod
    def get_sales():
        return sales
    # @staticmethod
    def create_sale(self):
        sale_id= len(sales) +1
        sale ={"sale_id":self.sale_id,"product_id":self.product_id,"product_name" :self.product_name,"price" :self.price,"attendant" :self.attendant,"total_sale":self.total_sale,"quantity":self.quantity}
        sales.append(sale)
        return sales

