from abc import ABC
from src.Items.item import Item


class Shoes(Item, ABC):
    def __init__(self, lvl, rarity_lvl):
        super().__init__(lvl, rarity_lvl)
        self.class_power = 0.30
