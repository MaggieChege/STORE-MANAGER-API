from flask import Flask,Blueprint
from flask_restful import Api,Resource
from app.api.v1.myviews.views import Products,Sales,Get_sale_id,Get_product_id
from app.api.v1.myviews.users import UserRegistration
# from instance.config import app_configuration

blue = Blueprint("api", __name__, url_prefix="/api/v1")
api=Api(blue)

api.add_resource(Products,"/products")
api.add_resource(Sales,"/sales")
api.add_resource(Get_sale_id,"/sales/<int:sale_id>")
api.add_resource(Get_product_id,"/products/<int:product_id>")
