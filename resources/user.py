from flask import Response, request
from flask_jwt_extended.utils import create_access_token, create_refresh_token
from flask_jwt_extended.view_decorators import jwt_required

from database.models import User
from flask_restful import Resource
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required

class UsersAdmin(Resource):
    @jwt_required()
    def post(self):
        body = request.get_json()
        user = User()

        user.username = body["username"]
        user.admin = body["admin"]
        print(user.admin)

        pw_hash = generate_password_hash(body["password"].encode('utf-8'), 10)
        user.password = pw_hash.decode('utf-8')

        user.save()

        return Response("User Added", mimetype="application/json", status=200)

    @jwt_required()
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)

    @jwt_required()
    def delete(self):
        User.objects().delete()

        return Response("Database Cleared", mimetype="application/json", status=420)


class UserLogin(Resource):
    def post(self):
        body = request.get_json()
        try:
            user = User.objects.get(username=body["username"])

        except Exception as e:
            print(e)
            return Response({body["username"], " failed login.",}, mimetype="application/json", status=403)

        checkPassword = (check_password_hash(user.password, body["password"]))

        try:
            if checkPassword & user.admin == True:
                access_token = create_access_token(identity=user.username)
                refresh_token = create_refresh_token(identity=user.username)

                res = {
                    "message": f'{user.username} logged in as administrator.',
                    "access_token": access_token,
                    "refresh_token": refresh_token
                }

                return res

            elif checkPassword == True & user.admin == False:
                return {
                    "message": f'{user.username} logged in as guest.'
                }
            elif checkPassword == False:
                return Response("Login Attempt Rejected", status=403)

        except Exception as e:
            print(e)
            return Response(status=418)
