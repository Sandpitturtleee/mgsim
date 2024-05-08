from abc import ABC
from src.Items.item import Item
from src.Items.weapons import Weapons


class Secondary(Weapons, ABC):
    weapon_factor = {
        "normal": [0.2406],
        "normal+wounds": [0.1897, 0.0367],
        "normal+poison": [0.1897, 0.0335],
    }
    damage_dispersion = {
        "normal": [0.1],
        "normal+wounds": [0.1, 1],
        "normal+poison": [0.1, 0],
    }

    slow_factor = {
        "poison": [0.006375],
    }

    def __init__(self, lvl, damage_type, rarity_factor):
        super().__init__(lvl, damage_type, rarity_factor)
