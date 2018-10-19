from flask import Flask,Blueprint
from flask_restful import Api,Resource
# from app.api.v1.myviews.users import Er
from app.api.v1.myviews.views import Products,Sales,Get_sale_id,Get_product_id
from app.api.v1.myviews.users import UserRegistration
 # UserLogin, TokenRefresh
from instance.config import app_configuration

blue = Blueprint("api", __name__, url_prefix="/api/v1")
api=Api(blue)


def create_app(config_name):
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_configuration['development'])
    app.register_blueprint(blue)



    api.add_resource(Products,"/products")
    api.add_resource(Sales,"/sales")
    api.add_resource(Get_sale_id,"/sales/<int:sale_id>")
    api.add_resource(Get_product_id,"/products/<int:product_id>")
    api.add_resource(UserRegistration,"/registration")
    # api.add_resource(Er,"/er")
    # api.add_resource(TokenRefresh,"/token")

    return app

