# Импорт необходимых библиотек
from flask import request
from flask_restx import Namespace, Resource

# Импорт схемы User
from dao.model.user import UserSchema

# Импорт декораторов
from decorators.utils import auth_required

# Импорт экземпляра класса UserService
from implemented import user_service

# Формирование нэймспейса
user_ns = Namespace('users')

# Формирование сереfлизаторов для модели User для одного элемента и для списка
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/<user_email>')
class UserView(Resource):
    @auth_required
    def get(self, user_email):
        """
            Формирование представления для получения пользователя по email
        """
        try:
            user = user_service.get_user(user_email)
            return user_schema.dump(user), 200
        except Exception:
            return "No such user", 404

    @auth_required
    def put(self, user_email):
        """
            Формирование представления для изменения данных пароля пользователя
        """
        try:
            data = request.json
            user_service.update_user(data, user_email)
            return '', 201
        except Exception:
            return 404

    @auth_required
    def patch(self, user_email):
        """
            Формирование представления для изменения данных пользователя
        """
        try:
            data = request.json
            user_service.update_user(data, user_email)
            return '', 201
        except Exception as e:
            return e

@user_ns.route('/')
class UsersView(Resource):
    def post(self):
        """
            Формирование представления для добавления нового пользователя
        """
        try:
            data = request.json
            user_service.create_user(data)
            return '', 201
        except Exception:
            return 404

