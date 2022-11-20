# Импорт необходимых библиотек
from flask import request
from flask_restx import Namespace, Resource
from jwt import PyJWTError

# Импорт схемы User
from dao.model.user import UserSchema

# Импорт декораторов
from decorators.utils import auth_required, get_token

# Импорт экземпляра класса UserService
from implemented import user_service

# Формирование нэймспейса
users_ns = Namespace('users')

# Формирование сериализаторов для модели User для одного элемента и для списка
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@users_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        """
            Формирование представления для получения пользователя по email
        """
        try:
            token = get_token()
            user_email = get('email')
            user = user_service.get_user(user_email)
            return user_schema.dump(user), 200
        except PyJWTError:
            print('Проверьте введенные данные')

    @auth_required
    def put(self):
        """
            Формирование представления для изменения данных пароля пользователя
        """
        try:
            data = request.json
            token = get_token()
            user_email = get('email')
            user_service.update_user(data, user_email)
            return '', 201
        except PyJWTError:
            print('Проверьте введенные данные')

    @auth_required
    def patch(self):
        """
            Формирование представления для изменения данных пользователя
        """
        try:
            data = request.json
            token = get_token()
            user_email = get('email')
            user_service.update_user(data, user_email)
            return '', 201
        except PyJWTError:
            print('Проверьте введенные данные')
