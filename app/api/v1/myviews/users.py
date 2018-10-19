from flask import request,Flask,jsonify, make_response
from flask_restful import Resource, reqparse

from functools import wraps
class UserRegistration(Resource):
    def get(self):
        if request.authorization and request.authorization.username == 'admin' and request.authorization.password == 'admin':
            return {"message":"hello"}
        return make_response('Not Verified',401,{"www-Authenticate": 'Basic realm="Login Required"'})



# class Er(Resource):
#     def auth_required(f):
#         @wraps(f)
#         def decorated(*args, **kwargs):
#             auth = request.authorization
#             if auth and auth.username == 'username' and auth.password == 'password':
#                 return f(*args, **kwargs)
#                 return make_response('Could not verify your login!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
#                 return decorated
#     @auth_required
#     def get(self):
#         return jsonify(er)
