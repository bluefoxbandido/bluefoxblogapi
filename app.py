from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from database.db import initialize_db
from resources.routes import initialize_routes

import os

load_dotenv()

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host' : os.getenv('MONGO_URI')
}

initialize_db(app)
initialize_routes(api)


if (__name__) == ('__main__'):
    app.run(debug=True)