import numpy as numpy
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, lvl_p: int, lvl_e: int):
        self.lvl_p = lvl_p
        self.lvl_e = lvl_e
        self.hp = self.calculate_hp()
        self.cr = self.calculate_cr()
        self.cg = self.calculate_cg()
        self.cd = self.calculate_cd()
        self.str = self.calculate_str()
        self.agi = self.calculate_agi()
        self.int = self.calculate_int()

    def calculate_hp(self):
        return 20 * min(self.lvl_e, 300) ** 1.375

    def calculate_cr(self):
        return 1 + 0.02 * self.lvl_e

    def calculate_cg(self):
        # min in documentation max makes sense
        return numpy.sign(self.lvl_p - self.lvl_e) * max(abs(self.lvl_p - self.lvl_e) - 5, 0) * 3

    def calculate_cd(self):
        # min in documentation max makes sense
        return numpy.sign(self.lvl_p - self.lvl_e) * max(abs(self.lvl_p - self.lvl_e) - 5, 0) * 10

    @abstractmethod
    def calculate_str(self):
        pass

    @abstractmethod
    def calculate_agi(self):
        pass

    @abstractmethod
    def calculate_int(self):
        pass
