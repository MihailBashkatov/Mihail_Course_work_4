import pytest
from service.genre import GenreService


class TestgenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_genre(5)
        assert genre is not None
        assert genre.id is not None
        assert genre.name == 'Кино'

    def test_get_all(self):
        genre = self.genre_service.get_genres()
        assert genre is not None
        assert type(genre) == list
        assert len(genre) == 3
