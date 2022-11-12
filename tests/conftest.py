from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name='Иванов')
    director_2 = Director(id=2, name='Петров')
    director_3 = Director(id=3, name='Сидоров')
    director_dao.get_director = MagicMock(return_value=director_1)
    director_dao.get_directors = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.create_director = MagicMock(return_value=Director(id=3, name='Сидоров'))
    director_dao.delete_director = MagicMock()
    director_dao.update_director = MagicMock(return_value=Director(id=4, name='Тютелькин'))
    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    genre_1 = Genre(id=1, name='Кино')
    genre_2 = Genre(id=2, name='Фильм')
    genre_3 = Genre(id=3, name='Мульт')
    genre_dao.get_genre = MagicMock(return_value=genre_1)
    genre_dao.get_genres = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.create = MagicMock(return_value=Genre(id=3, name='Мульт'))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock(return_value=Genre(id=4, name='Док'))
    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    movie_1 = Movie(id=1, title='Кино')
    movie_2 = Movie(id=2, title='Фильм')
    movie_3 = Movie(id=3, title='Мульт')
    movie_dao.get_movie = MagicMock(return_value=movie_1)
    movie_dao.get_movies = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create_movie = MagicMock(return_value=Movie(id=3, title='Мульт'))
    movie_dao.delete_movie = MagicMock()
    movie_dao.update_movie = MagicMock(return_value=Movie(id=4, title='Док'))
    return movie_dao
