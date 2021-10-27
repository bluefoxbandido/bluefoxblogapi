from flask import Response, request

from database.models import User
from flask_restful import Resource
from flask_bcrypt import generate_password_hash, check_password_hash

class UsersAdmin(Resource):
    def post(self):
        body = request.get_json()
        user = User()

        user.username = body["username"]
        user.admin = body["admin"]

        pw_hash = generate_password_hash(body["password"].encode('utf-8'), 10)
        user.password = pw_hash.decode('utf-8')

        user.save()
        
        return Response(user, mimetype="application/json", status=200)
    
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)
    
    def delete(self):
        User.objects().delete()

        return "Database Cleared"
    
class UserLogin(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(username = body["username"])
        
        
        return check_password_hash(user.password, body["password"])

        