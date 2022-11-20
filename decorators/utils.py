# Импорт необходимых библиотек
import jwt
from flask import request, abort
from constants import algo, secret


def auth_required(func):
    """
        Декоратор проверки авторизации
    """
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        get_token()
        return func(*args, **kwargs)
    return wrapper


def get_token():
    """
        Получение
    """
    data = request.headers['Authorization']
    token = data.split("Bearer ")[-1]
    token_decoded = jwt.decode(token, secret, algorithms=[algo])
    return token_decoded
