class MovieService:

    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def get_movies(self, param, data):
        """
            Формирование запроса в зависимости от параметров поиска
        """
        movies = self.movie_dao.get_movies()
        if param == 'status':
            movies = self.movie_dao.get_movies_by_new()
        if param == 'page':
            movies = self.movie_dao.get_movies_by_page(int(data))
        return movies

    def get_movie(self, mid):
        """
            Получение фильма по id
        """
        return self.movie_dao.get_movie(mid)
