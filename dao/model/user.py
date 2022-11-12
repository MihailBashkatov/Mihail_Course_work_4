# Импорт необходимых библиотек
from marshmallow import Schema, fields

# Импорт базы данных
from dao.model.genre import GenreSchema
from setup_db import db


# Формирование класса User
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship('Genre')


# Формирование схемы User
class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    genre = fields.Pluck(field_name='name', nested=GenreSchema)
