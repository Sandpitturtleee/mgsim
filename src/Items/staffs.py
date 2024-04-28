from abc import ABC
from src.Items.item import Item


class Staffs(Item, ABC):
    def __init__(self, lvl, rarity_lvl):
        super().__init__(lvl, rarity_lvl)
        self.class_power = 1.00
        self.weapon_factor = {
            "fire": 0.3188,
            "frost": 0.2709,
            "thunder": 0.3652,
        }
        self.damage_dispersion = {
            "fire": 0.2,
            "frost": 0,
            "thunder": 0.2,
        }
