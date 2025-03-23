import pytest

from src.character.professions.hunter import Hunter


class TestHunter:
    @pytest.fixture
    def hunter(self):
        return Hunter(character_lvl=53, enemy_lvl=53)

    def test_calculate_attributes(self, hunter):
        expected_attributes = {"strength": 23, "agility": 244, "intellect": 3}
        assert hunter.character_attributes_lvl == expected_attributes

    def test_calculate_strength(self, hunter):
        assert hunter.character_attributes_lvl["strength"] == 23

    def test_calculate_agility(self, hunter):
        assert hunter.character_attributes_lvl["agility"] == 244

    def test_calculate_intelligence(self, hunter):
        assert hunter.character_attributes_lvl["intellect"] == 3
