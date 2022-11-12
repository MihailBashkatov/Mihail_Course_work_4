import pytest
from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_movie(5)
        assert movie is not None
        assert movie.id is not None
        assert movie.title == 'Кино'

    def test_get_all(self):
        movie = self.movie_service.get_movies(param=None, data=None)
        assert movie is not None
        assert type(movie) == list
        assert len(movie) == 3
