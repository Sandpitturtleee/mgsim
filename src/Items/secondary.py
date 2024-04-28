from abc import ABC
from src.Items.item import Item


class Secondary(Item, ABC):
    def __init__(self, lvl, rarity_lvl):
        super().__init__(lvl, rarity_lvl)
        self.class_power = 1.00
        self.weapon_factor = {
            "normal": 0.2406,
            "normal+wounds": [0.1897,0.0367],
            "normal+poison": [0.1897,0.0335],
        }
        self.damage_dispersion = {
            "normal": 0.1,
            "normal+wounds": [0.1, 1],
            "normal+poison": [0.1, 0],
        }
