import pytest

from src.character.professions.blade_dancer import BladeDancer


class TestWarrior:
    @pytest.fixture
    def blade_dancer(self):
        return BladeDancer(character_lvl=53, enemy_lvl=53)

    def test_calculate_attributes(self, blade_dancer):
        expected_attributes = {"strength": 144, "agility": 123, "intellect": 3}
        assert blade_dancer.character_attributes_lvl == expected_attributes

    def test_calculate_strength(self, blade_dancer):
        assert blade_dancer.character_attributes_lvl["strength"] == 144

    def test_calculate_agility(self, blade_dancer):
        assert blade_dancer.character_attributes_lvl["agility"] == 123

    def test_calculate_intelligence(self, blade_dancer):
        assert blade_dancer.character_attributes_lvl["intellect"] == 3
