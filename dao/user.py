from dao.model.user import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_user(self, user_email):
        """
            Получение пользователя по username
        """
        return self.session.query(User).filter(User.email == user_email).one()

    def delete_user(self, user_name):
        """
            Удаление пользователя
        """
        user = self.get_user(user_name)
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

    def update_user(self, data, user_name):
        """
            Обновление пароля пользователя
        """
        self.session.query(User).filter(User.name == user_name).update(data)
        self.session.commit()


    def get_all(self):
        """
            Получение всех пользователей
        """
        users = self.session.query(User).all()
        return users
