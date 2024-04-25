import numpy as numpy


class Player:
    def __init__(self, lvl_p: int, lvl_e: int):
        self.lvl_p = lvl_p
        self.lvl_e = lvl_e
        self.hp = self.calculate_hp()
        self.cr = self.calculate_cr()
        self.cg = self.calculate_cg()

    def calculate_hp(self):
        return 20 * min(self.lvl_e, 300) ** 1.375

    def calculate_cr(self):
        return 1 + 0.02 * self.lvl_e

    def calculate_cg(self):
        # min in documentation max makes sense
        return numpy.sign(self.lvl_p - self.lvl_e) * max(abs(self.lvl_p - self.lvl_e) - 5, 0) * 3

