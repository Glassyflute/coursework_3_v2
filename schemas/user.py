from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    role = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()   # id or genre's name TBD, one or multiple TBD



    # username = fields.Str()
    # password = fields.Str()
    # role = fields.Str()
