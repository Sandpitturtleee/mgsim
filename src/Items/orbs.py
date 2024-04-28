from abc import ABC
from src.Items.item import Item


class Orbs(Item, ABC):
    def __init__(self, lvl, rarity_lvl):
        super().__init__(lvl, rarity_lvl)
        self.class_power = 1.00
        self.weapon_factor = {
            "fire": 0.1514,
            "frost": 0.1355,
            "thunder": 0.1528,
        }
        self.damage_dispersion = {
            "fire": 0.2,
            "frost": 0,
            "thunder": 0.2,
        }
