import pytest

from service.director import DirectorService


class TestdirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        director = self.director_service.get_director(5)
        assert director is not None
        assert director.id is not None
        assert director.name == 'Иванов'

    def test_get_all(self):
        director = self.director_service.get_directors()
        assert director is not None
        assert type(director) == list
        assert len(director) == 3
