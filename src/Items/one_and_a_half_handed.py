from abc import ABC
from src.Items.item import Item
from src.Items.weapons import Weapons


class OneAndAHalfHanded(Weapons, ABC):
    weapon_factor = {
        "normal": [0.3964],
        "normal+wounds": [0.3267, 0.1084],
        "normal+poison": [0.3267, 0.0797],
        "normal+fire": [0.4016, 0.2072],
        "normal+frost": [0.4016, 0.1865],
        "normal+thunder": [0.4016, 0.2072],
    }
    damage_dispersion = {
        "normal": [0.1],
        "normal+wounds": [0.1, 1],
        "normal+poison": [0.1, 0],
        "normal+fire": [0.1, 0.2],
        "normal+frost": [0.1, 0],
        "normal+thunder": [0.1, 0.2],
    }

    slow_factor = {
        "frost": [0.010000],
        "poison": [0.008925],
    }

    def __init__(self, lvl, damage_type, rarity_factor):
        super().__init__(lvl, damage_type, rarity_factor)
