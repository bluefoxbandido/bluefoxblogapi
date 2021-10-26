from .db import db
from datetime import datetime

class Blog(db.Document):
    title = db.StringField(required=True, unique=True)
    date = db.StringField(default=datetime.now().strftime("%D %H:%M:%S"))
    blogBody = db.StringField(required=True)
    imageUrl = db.StringField()