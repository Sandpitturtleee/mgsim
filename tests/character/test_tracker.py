import pytest

from src.character.professions.tracker import Tracker


class TestTracker:
    @pytest.fixture
    def tracker(self):
        return Tracker(character_lvl=64, enemy_lvl=64)

    def test_calculate_attributes(self, tracker):
        expected_attributes = {"strength": 23, "agility": 151, "intellect": 151}
        assert tracker.character_attributes_lvl == expected_attributes

    def test_calculate_strength(self, tracker):
        assert tracker.character_attributes_lvl["strength"] == 23

    def test_calculate_agility(self, tracker):
        assert tracker.character_attributes_lvl["agility"] == 151

    def test_calculate_intelligence(self, tracker):
        assert tracker.character_attributes_lvl["intellect"] == 151
