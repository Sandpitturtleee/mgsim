import math

import numpy as numpy
from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, lvl: int, rarity_factor: int):
        self.lvl = lvl
        self.rarity_factor = rarity_factor  # 0,1,2,3,4
        self.lvl_power = self.calculate_lvl_power()
        self.rarity_power = self.calculate_rarity_power()

    def calculate_lvl_power(self):
        return 0.02 * self.lvl**2 + 2.6 * self.lvl

    def calculate_rarity_power(self):
        return 0.02 * self.lvl * math.ceil(10 * self.rarity_factor / 3) + numpy.sign(
            self.rarity_factor
        ) * (7.8 * self.rarity_factor + 2.6)
