from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_directors(self):
        """
            Получение всех директоров
        """
        return self.session.query(Director).all()

    def get_director(self, did):
        """
            Получение диерктора по id
        """
        return self.session.query(Director).filter(Director.id == did).one()
