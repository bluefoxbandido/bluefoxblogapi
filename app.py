from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from waitress import serve
from flask_cors import CORS, cross_origin

from database.db import initialize_db
from resources.routes import initialize_routes

import os



app = Flask(__name__)
CORS(app)
api = Api(app)



app.config['MONGODB_SETTINGS'] = {
    'host' : os.environ['MONGO_URI']
}

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']


initialize_db(app)
initialize_routes(api)

jwt = JWTManager(app)

if (__name__) == ('__main__'):
    try:
        serve(app, port=5000, url_scheme='https')
    except:
        print("Error launching server.")