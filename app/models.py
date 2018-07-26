from app import db
from mongoengine import StringField, DateTimeField, Document
from werkzeug.security import check_password_hash, generate_password_hash
import datetime


class User(Document):
    """
    Model Representing the user.
    """
    email = StringField(unique=True, required=True)
    password = StringField(required=True)
    name = StringField(required=True)
    last_name = StringField(required=True)
    date_created = DateTimeField()
    date_modified = DateTimeField(default=datetime.datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.id}:{self.email}>'
