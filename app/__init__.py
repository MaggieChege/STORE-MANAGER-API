from flask import Flask,Blueprint
# from instance.config import app_configuration
from flask_jwt_extended import JWTManager


def create_app(config_name):
    app=Flask(__name__,instance_relative_config=True)
    # app.config.from_object(app_configuration['development'])
    from app.api.v1 import blue as v1
    app.register_blueprint(v1)
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    jwt = JWTManager(app)




    return app
