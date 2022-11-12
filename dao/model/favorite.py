# Импорт необходимых библиотек
from marshmallow import Schema, fields

# Импорт базы данных
from dao.model.movie import MovieSchema
from dao.model.user import UserSchema
from setup_db import db


# Формирование класса Director
class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    # user = db.relationship('User')
    movie = db.relationship('Movie')

# Формирование схемы Director
class FavoriteSchema(Schema):
    id = fields.Int()
    # user = fields.Pluck(field_name='name', nested=UserSchema)
    movie = fields.Pluck(field_name='description', nested=MovieSchema)


