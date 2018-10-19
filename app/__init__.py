from flask import Flask,Blueprint
# from instance.config import app_configuration



def create_app(config_name):
    app=Flask(__name__,instance_relative_config=True)
    # app.config.from_object(app_configuration['development'])
    from app.api.v1 import blue as v1
    app.register_blueprint(v1)




    return app
