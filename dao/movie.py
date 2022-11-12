from sqlalchemy import desc

from dao.model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_movies(self):
        """
            Получение всех фильмов
        """
        movies = self.session.query(Movie).all()
        return movies

    def get_movies_by_new(self):
        """
            Получение фильмов по году
        """
        movies = self.session.query(Movie).order_by(desc(Movie.year))
        return movies

    def get_movies_by_page(self, page):
        movies = Movie.query.limit(5).offset(page * 5 - 5)
        return movies

    def get_movie(self, mid):
        """
            Получение фильма по id
        """
        movie = self.session.query(Movie).filter(Movie.id == mid).one()
        return movie
