# Импорт необходимых библиотек
from flask_restx import Resource, Namespace

# Импорт схемы Director
from dao.model.director import DirectorSchema

# Импорт декораторов
from decorators.utils import auth_required

# Импорт экземпляра класса DirectorService
from implemented import director_service

# Формирование нэймспейса
director_ns = Namespace('directors')

# Формирование сереилизаторов для модели Director для одного элемента и для списка
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """
            Формирование представления для получения режиссеров
        """
        try:
            directors = director_service.get_directors()
            return directors_schema.dump(directors), 200
        except Exception as e:
            return e


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        """
            Формирование представления для получения режиссера по id
        """
        try:
            director = director_service.get_director(did)
            return director_schema.dump(director), 200
        except Exception:
            return 404
