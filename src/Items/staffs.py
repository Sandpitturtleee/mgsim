from abc import ABC
from src.Items.item import Item
from src.Items.weapons import Weapons


class Staffs(Weapons, ABC):
    weapon_factor = {
        "fire": [0.3188],
        "frost": [0.2709],
        "thunder": [0.3652],
    }
    damage_dispersion = {
        "fire": [0.2],
        "frost": [0],
        "thunder": [0.2],
    }
    slow_factor = {
        "frost": [0.010000],
    }

    def __init__(self, lvl, player, damage_type, rarity_factor):
        super().__init__(lvl, player, damage_type, rarity_factor)
