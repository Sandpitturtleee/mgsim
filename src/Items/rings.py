from abc import ABC
from src.Items.item import Item


class Rings(Item, ABC):
    def __init__(self, lvl, rarity_lvl):
        super().__init__(lvl, rarity_lvl)
        self.class_power = 1.00
        self.rarity_factor = rarity_lvl
