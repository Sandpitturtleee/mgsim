from abc import ABC
from src.Items.item import Item


class OneHanded(Item, ABC):
    def __init__(self, lvl, rarity_lvl):
        super().__init__(lvl, rarity_lvl)
        self.class_power = 1.00
        self.weapon_factor = {
            "normal": 0.3378,
            "normal+wounds": [0.2646, 0.0876],
            "normal+poison": [0.2646, 0.0797],
            "normal+fire": [0.2869, 0.1594],
            "normal+frost": [0.2869, 0.1435],
            "normal+thunder": [0.2869, 0.1594],
        }
        self.damage_dispersion = {
            "normal": 0.1,
            "normal+wounds": [0.1, 1],
            "normal+poison": [0.1, 0],
            "normal+fire": [0.1, 0.2],
            "normal+frost": [0.1, 0],
            "normal+thunder": [0.1, 0.2],
        }

