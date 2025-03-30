from abc import abstractmethod

import numpy


class LvlAttributes:
    def __init__(self, character_lvl, enemy_lvl):
        # Poziom postaci
        self.character_lvl = character_lvl  # character
        self.enemy_lvl = enemy_lvl  # przeciwnik
        self.hp_lvl = self.calculate_hp_lvl()
        self.character_attributes_lvl = (
            self.calculate_attributes_lvl()
        )  # sila zreczonsc intelekt
        self.crit_lvl = self.calculate_crit_lvl()  # crit
        self.crit_gain_lvl = self.calculate_crit_gain_lvl()  # crit gain
        self.crit_val_gain_lvl = (
            self.calculate_crit_val_gain_lvl()
        )  # sila ciosu krytycznego magicznego/fizycznego

    def calculate_hp_lvl(self):
        return 20 * min(self.character_lvl, 300) ** 1.375

    @abstractmethod
    def calculate_attributes_lvl(self):
        pass

    def calculate_crit_lvl(self):
        return 1 + 0.02 * self.enemy_lvl

    def calculate_crit_gain_lvl(self):
        # min in documentation max makes sense
        return (
                numpy.sign(self.character_lvl - self.enemy_lvl)
                * max(abs(self.character_lvl - self.enemy_lvl) - 5, 0)
                * 3
        )

    def calculate_crit_val_gain_lvl(self):
        # min in documentation max makes sense
        return (
                numpy.sign(self.character_lvl - self.enemy_lvl)
                * max(abs(self.character_lvl - self.enemy_lvl) - 5, 0)
                * 10
        )
