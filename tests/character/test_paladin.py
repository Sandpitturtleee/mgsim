import pytest

from src.character.professions.paladin import Paladin


class TestPaladin:
    @pytest.fixture
    def paladin(self):
        return Paladin(character_lvl=70, enemy_lvl=70)

    def test_calculate_attributes(self, paladin):
        expected_attributes = {"strength": 176, "agility": 13, "intellect": 166}
        assert paladin.character_attributes_lvl == expected_attributes

    def test_calculate_strength(self, paladin):
        assert paladin.character_attributes_lvl["strength"] == 176

    def test_calculate_agility(self, paladin):
        assert paladin.character_attributes_lvl["agility"] == 13

    def test_calculate_intelligence(self, paladin):
        assert paladin.character_attributes_lvl["intellect"] == 166
