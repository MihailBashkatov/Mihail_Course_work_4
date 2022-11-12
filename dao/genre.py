from dao.model.genre import Genre
from setup_db import db

class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_genre(self, gid):
        """
            Получение жанра по id
        """
        return self.session.query(Genre).filter(Genre.id == gid).one()

    def get_genres(self):
        """
            Получение всех жанров
        """
        return self.session.query(Genre).all()
