from abc import ABC
from src.Items.item import Item


class Quivers(Item, ABC):
    def __init__(self, lvl, rarity_lvl):
        super().__init__(lvl, rarity_lvl)
        self.class_power = 1.00
        self.weapon_factor = {
            "normal": 0.0303,
            "poison": 0.0271,
            "fire": 0.0478,
            "frost": 0.0430,
            "thunder": 0.0478,
        }
        self.damage_dispersion = {
            "normal": 0.1,
            "poison": 0,
            "fire": 0.2,
            "frost": 0,
            "thunder": 0.2,
        }
