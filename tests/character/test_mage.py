import pytest

from src.character.professions.mage import Mage


class TestMage:
    @pytest.fixture
    def mage(self):
        return Mage(character_lvl=53, enemy_lvl=53)

    def test_calculate_attributes(self, mage):
        expected_attributes = {"strength": 23, "agility": 22, "intellect": 225}
        assert mage.character_attributes_lvl == expected_attributes

    def test_calculate_strength(self, mage):
        assert mage.character_attributes_lvl["strength"] == 23

    def test_calculate_agility(self, mage):
        assert mage.character_attributes_lvl["agility"] == 22

    def test_calculate_intelligence(self, mage):
        assert mage.character_attributes_lvl["intellect"] == 225
