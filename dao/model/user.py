from marshmallow import Schema, fields
from setup_db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)     # nullable or not?
    name = db.Column(db.String(255))    # saved in hashed version
    surname = db.Column(db.String(255))
    favorite_genre = db.Column(db.String)   # id or genre's name TBD, one or multiple TBD

    # username = db.Column(db.String, unique=True, nullable=False)
    # password = db.Column(db.String, nullable=False)
    # role = db.Column(db.String, nullable=False)



# class UserSchema(Schema):
#     id = fields.Int()
#     username = fields.Str()
#     password = fields.Str()
#     role = fields.Str()
