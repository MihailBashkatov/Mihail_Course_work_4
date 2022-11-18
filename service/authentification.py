# Импорт необходимых биьлиотек
import calendar
import datetime
from flask import abort
import jwt
from jwt import PyJWTError

# Импорт констант
from constants import algo, secret


class AuthentificaionService:
    def __init__(self, user_service):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        """
            Генерация токенов
        """
        user = self.user_service.get_user(email)

        if user is None:
            abort(401)

        # Проверка на обновление токенов (is_refresh=True) или формирование изначальных (is_refresh=False)
        # Сравнение введенного и хэшированного паролей
        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(401)
        try:
            data = {"eamil": user.email}

            # Формирование срока действия токенов
            min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            data["exp"] = calendar.timegm(min30.timetuple())
            access_token = jwt.encode(data, secret, algorithm=algo)
            days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
            data["exp"] = calendar.timegm(days130.timetuple())
            refresh_token = jwt.encode(data, secret, algorithm=algo)
            tokens = {"access_token": access_token, "refresh_token": refresh_token}
            return tokens
        except PyJWTError:
            print('Проверьте введенные данные')

    def update_tokens(self, token):
        """
            Обновление токенов по refresh_token
        """
        user_data = jwt.decode(jwt=token, key=secret, algorithms=[algo])
        email = user_data.get('email')
        return self.generate_tokens(email, None, is_refresh=True)
