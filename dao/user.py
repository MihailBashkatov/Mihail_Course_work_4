from dao.model.user import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_user(self, email):
        """
            Получение пользователя по username
        """
        return self.session.query(User).filter(User.email == email).first()

    def delete_user(self, email):
        """
            Удаление пользователя
        """
        user = self.get_user(email)
        self.session.delete(user)
        self.session.commit()

    def create_user(self, data):
        """
            Создание пользователя
        """
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update_user(self, data, email):
        """
            Обновление пароля пользователя
        """
        self.session.query(User).filter(User.name == email).update(data)
        self.session.commit()

    def get_all(self):
        """
            Получение всех пользователей
        """
        users = self.session.query(User).all()
        return users
