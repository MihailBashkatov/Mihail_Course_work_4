# Импорт необходимых библиотек
from flask import request, abort
from flask_restx import Namespace, Resource

# Импорт экземпляра класса AuthentificationService
from implemented import authentification_service, user_service

# Формирование нэймспейса
auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthView(Resource):
    @staticmethod
    def post():
        """
            Регистрация пользователя по username and password
        """
        data = request.json
        user_service.create_user(data)
        return '', 201


@auth_ns.route('/login/')
class LoginView(Resource):
    """
        Аутентификация и авторизация пользователя по user_email and password
    """
    @staticmethod
    def post():
        data = request.json
        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            abort(401)

        # Получение токенов
        tokens = authentification_service.generate_tokens(email, password)
        return tokens, 201

    @staticmethod
    def put():
        """
            Обновление refresh_token
        """
        request_json = request.json
        refresh_token = request_json.get("refresh_token")
        tokens = authentification_service.update_tokens(refresh_token)
        return tokens
