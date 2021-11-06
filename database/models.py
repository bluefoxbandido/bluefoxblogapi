from .db import db
from datetime import datetime


class Blog(db.Document):
    title = db.StringField(required=True, unique=True)
    subheading = db.StringField(required=True)
    date = db.StringField(default=datetime.now().strftime("%D %H:%M:%S"))
    content = db.DynamicField()
    image = db.DynamicField()
    color = db.StringField()

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    email = db.StringField(required=True, unique=True)
    password = db.DynamicField(required=True)
    admin = db.BooleanField(default=False)

class Service(db.Document):
    name = db.StringField(required=True, unique=True)
    description = db.StringField(required=True)
    source_code = db.StringField()
    thumbnail = db.DynamicField()
    overview = db.DynamicField()

class About(db.Document):
    biography = db.DynamicField()
    quote = db.StringField()
    avatar = db.DynamicField()