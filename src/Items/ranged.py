from abc import ABC
from src.Items.item import Item


class Ranged(Item, ABC):
    def __init__(self, lvl, rarity_lvl):
        super().__init__(lvl, rarity_lvl)
        self.class_power = 1.00
        self.weapon_factor = {
            "normal": 0.4303,
            "normal+wounds": [0.2901,0.1036],
            "normal+poison": [0.2901,0.1116],
            "normal+fire": [0.2231,0.2263],
            "normal+frost": [0.2231,0.2040],
            "normal+thunder": [0.2231,0.2258],
        }
        self.damage_dispersion = {
            "normal": 0.1,
            "normal+wounds": [0.1, 1],
            "normal+poison": [0.1, 0],
            "normal+fire": [0.1, 0.2],
            "normal+frost": [0.1, 0],
            "normal+thunder": [0.1, 0.2],
        }