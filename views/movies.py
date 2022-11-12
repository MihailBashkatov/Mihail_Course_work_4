# Импорт необходимых библиотек
from flask import request
from flask_restx import Resource, Namespace

# Импорт схемы Movie
from dao.model.movie import MovieSchema

# Импорт декораторов
from decorators.utils import auth_required

# Импорт экземпляра класса MovieService
from implemented import movie_service

# Формирование нэймспейса
movies_ns = Namespace('movies')

# Формирование сереилизаторов для модели Movie для одного элемента и для списка
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
            Формирование представления для получения фильмов
        """
        try:
            param = None
            data = None
            status = request.args.get('status')
            page = request.args.get('page')
            if status:
                param = 'status'
            if page:
                param = 'page'
                data = page
            movies = movie_service.get_movies(param, data)
            movies_list = movies_schema.dump(movies)
            return movies_list, 200
        except Exception as e:
            return e


@movies_ns.route('/<mid>/')
class MovieView(Resource):
    @auth_required
    def get(self, mid):
        """
            Формирование представления для получения фильма по id
            В случае отсутствия фильма возвращается 'No such movie'
        """
        try:
            movie = movie_service.get_movie(mid)
            return movie_schema.dump(movie), 200
        except Exception:
            return 404
