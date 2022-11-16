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
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        jwt.decode(token, secret, algorithms=[algo])

        return func(*args, **kwargs)
    return wrapper
