from abc import ABC
from src.Items.item import Item


class TwoHanded(Item, ABC):
    def __init__(self, lvl, rarity_lvl):
        super().__init__(lvl, rarity_lvl)
        self.class_power = 1.00
        self.weapon_factor = {
            "normal": 0.5578,
            "normal+wounds": [0.4606, 0.1530],
            "normal+poison": [0.4606, 0.0797],
            "normal+fire": [0.4876, 0.2390],
            "normal+frost": [0.4876, 0.2152],
            "normal+thunder": [0.4876, 0.2391],
        }
        self.damage_dispersion = {
            "normal": 0.1,
            "normal+wounds": [0.1, 1],
            "normal+poison": [0.1, 0],
            "normal+fire": [0.1, 0.2],
            "normal+frost": [0.1, 0],
            "normal+thunder": [0.1, 0.2],
        }
