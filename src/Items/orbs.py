from abc import ABC
from src.Items.item import Item
from src.Items.weapons import Weapons


class Orbs(Weapons, ABC):
    weapon_factor = {
        "fire": [0.1514],
        "frost": [0.1355],
        "thunder": [0.1528],
    }
    damage_dispersion = {
        "fire": [0.2],
        "frost": [0],
        "thunder": [0.2],
    }
    slow_factor = {
        "frost": [0.0073529],
    }

    def __init__(self, lvl, damage_type, rarity_factor):
        super().__init__(lvl, damage_type, rarity_factor)
