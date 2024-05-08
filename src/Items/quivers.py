from abc import ABC
from src.Items.item import Item
from src.Items.weapons import Weapons


class Quivers(Weapons, ABC):
    weapon_factor = {
        "normal": [0.0303],
        "poison": [0.0271],
        "fire": [0.0478],
        "frost": [0.0430],
        "thunder": [0.0478],
    }
    damage_dispersion = {
        "normal": [0.1],
        "poison": [0],
        "fire": [0.2],
        "frost": [0],
        "thunder": [0.2],
    }

    slow_factor = {
        "frost": [0.0073529],
        "poison": [0.0044625],
    }

    def __init__(self, lvl,player, damage_type, rarity_factor):
        super().__init__(lvl, player,damage_type, rarity_factor)
        self.armor_destruction = self.calculate_armor_destruction()


    def calculate_armor_destruction(self):
        if self.player == "hunter":
            return 0.04 * self.lvl_power