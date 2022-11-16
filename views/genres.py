# Импорт необходимых библиотек
from flask_restx import Resource, Namespace

# Импорт схемы Genre
from dao.model.genre import GenreSchema

# Импорт декораторов
from decorators.utils import auth_required

# Импорт экземпляра класса GenreService
from implemented import genre_service

# Формирование нэймспейса
genre_ns = Namespace('genres')

# Формирование сереилизаторов для модели Genre для одного элемента и для списка
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """
            Формирование представления для получения жанров
        """

        genres = genre_service.get_genres()
        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:gid>/')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        """
            Формирование представления для получения жанра по id
        """

        genre = genre_service.get_genre(gid)
        return genre_schema.dump(genre), 200
