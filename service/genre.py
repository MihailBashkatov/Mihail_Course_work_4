class GenreService:
    def __init__(self, genre_dao):
        self.genre_dao = genre_dao

    def get_genres(self):
        """
            Получение всех жанров
        """
        return self.genre_dao.get_genres()

    def get_genre(self, gid):
        """
            Получение жанра по id
        """
        return self.genre_dao.get_genre(gid)
