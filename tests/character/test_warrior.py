import pytest

from src.character.professions.warrior import Warrior


class TestWarrior:
    @pytest.fixture
    def warrior(self):
        return Warrior(character_lvl=53, enemy_lvl=53)

    def test_calculate_attributes(self, warrior):
        expected_attributes = {"strength": 245, "agility": 22, "intellect": 3}
        assert warrior.character_attributes_lvl == expected_attributes

    def test_calculate_strength(self, warrior):
        assert warrior.character_attributes_lvl["strength"] == 245

    def test_calculate_agility(self, warrior):
        assert warrior.character_attributes_lvl["agility"] == 22

    def test_calculate_intelligence(self, warrior):
        assert warrior.character_attributes_lvl["intellect"] == 3
