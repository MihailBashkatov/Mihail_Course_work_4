class DirectorService:
    def __init__(self, director_dao):
        self.director_dao = director_dao

    def get_directors(self):
        """
            Получение всех директоров
        """
        return self.director_dao.get_directors()

    def get_director(self, did):
        """
            Получение директора по id
        """
        return self.director_dao.get_director(did)
