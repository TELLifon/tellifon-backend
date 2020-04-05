from datetime import datetime
from .db import db
import mongoengine_goodjson as gj


class Translation(gj.EmbeddedDocument):
    de = db.StringField(required=True, unique=False)
    en = db.StringField(required=True, unique=False)
    fr = db.StringField(required=True, unique=False)
    it = db.StringField(required=True, unique=False)
    rm = db.StringField(required=True, unique=False)

class Category(gj.Document):
    icon = db.StringField(required=True, unique=False)
    label = db.EmbeddedDocumentField(Translation)

class Event(gj.Document):
    name = db.StringField(required=True, unique=False)
    category_id = db.ReferenceField(Category)
    moderator = db.StringField(required=False, unique=False)
    starttime = db.DateTimeField(required=True, unique=False)
    endtime = db.DateTimeField(required=True, unique=False)
    description = db.StringField(required=False, unique=False)
    is_public = db.BooleanField(required=True, unique=False)
    img_src = db.StringField(required=False, unique=False)


