import numpy as numpy
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, lvl_p: int, lvl_e: int):
        self.lvl_p = lvl_p
        self.lvl_e = lvl_e
        self.str = self.calculate_str()
        self.agi = self.calculate_agi()
        self.int = self.calculate_int()
        self.hp = self.calculate_hp_lvl() + self.calculate_hp_str()
        self.sa = self.calculate_sa()
        self.evade_gain = self.calculate_evade_gain()
        self.cr = self.calculate_cr()
        self.cg = self.calculate_cg()
        self.cd_f = 120 + self.calculate_cd() + self.calculate_cd_f()
        self.cd_m = 120 + self.calculate_cd() + self.calculate_cd_m()
        self.abs_f_limit = self.calculate_abs_limit()
        self.abs_m_limit = self.calculate_abs_limit()

    def calculate_evade_gain(self):
        return self.agi / 30

    def calculate_sa(self):
        return min(2, 0.02 * self.agi) + max(0, 0.002 * (self.agi - 100))

    def calculate_abs_limit(self):
        return self.int * 7

    def calculate_cd_f(self):
        return self.str / (0.5 * self.lvl_p)

    def calculate_cd_m(self):
        return self.int / (0.5 * self.lvl_p)

    def calculate_hp_lvl(self):
        return 20 * min(self.lvl_p, 300) ** 1.375

    def calculate_hp_str(self):
        return self.str * 5

    def calculate_cr(self):
        return 1 + 0.02 * self.lvl_e

    def calculate_cg(self):
        # min in documentation max makes sense
        return (
            numpy.sign(self.lvl_p - self.lvl_e)
            * max(abs(self.lvl_p - self.lvl_e) - 5, 0)
            * 3
        )

    def calculate_cd(self):
        # min in documentation max makes sense
        return (
            numpy.sign(self.lvl_p - self.lvl_e)
            * max(abs(self.lvl_p - self.lvl_e) - 5, 0)
            * 10
        )

    @abstractmethod
    def calculate_str(self):
        pass

    @abstractmethod
    def calculate_agi(self):
        pass

    @abstractmethod
    def calculate_int(self):
        pass
