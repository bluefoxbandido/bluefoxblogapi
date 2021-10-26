from flask import Response, request
from database.models import User
from flask_restful import Resource

import hashlib
import os

class UsersAdmin(Resource):
    def post(self):
        body = request.get_json()
        user = User()

        user.username = body["username"]
        user.admin = body["admin"]

        salt = os.urandom(32)
        password = body["password"]
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        )        

        user.password = salt + key

        user.save()

        return "success"

# class UserLogin(Resource):
#     def post(username, password):
        