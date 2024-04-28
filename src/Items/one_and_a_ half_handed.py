from abc import ABC
from src.Items.item import Item


class OneAndAHalfHanded(Item, ABC):
    def __init__(self, lvl, rarity_lvl):
        super().__init__(lvl, rarity_lvl)
        self.class_power = 1.00
        self.weapon_factor = {
            "normal": 0.3964,
            "normal+wounds": [0.3267,0.1084],
            "normal+poison": [0.3267,0.0797],
            "normal+fire": [0.4016,0.2072],
            "normal+frost": [0.4016,0.1865],
            "normal+thunder": [0.4016,0.2072],
        }
        self.damage_dispersion = {
            "normal": 0.1,
            "normal+wounds": [0.1, 1],
            "normal+poison": [0.1, 0],
            "normal+fire": [0.1, 0.2],
            "normal+frost": [0.1, 0],
            "normal+thunder": [0.1, 0.2],
        }