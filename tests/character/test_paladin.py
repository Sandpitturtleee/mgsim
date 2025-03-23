import pytest

from src.character.professions.paladin import Paladin


class TestPaladin:
    @pytest.fixture
    def paladin(self):
        return Paladin(character_lvl=53, enemy_lvl=53)

    def test_calculate_attributes(self, paladin):
        expected_attributes = {"strength": 134, "agility": 13, "intellect": 123}
        assert paladin.character_attributes_lvl == expected_attributes

    def test_calculate_strength(self, paladin):
        assert paladin.character_attributes_lvl["strength"] == 134

    def test_calculate_agility(self, paladin):
        assert paladin.character_attributes_lvl["agility"] == 13

    def test_calculate_intelligence(self, paladin):
        assert paladin.character_attributes_lvl["intellect"] == 123
