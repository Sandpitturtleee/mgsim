from abc import ABC

from src.Player.character import Character


class Paladin(Character, ABC):
    def __init__(self, lvl_p: int, lvl_e: int):
        super().__init__(lvl_p, lvl_e)
        self.str = self.calculate_str()
        self.agi = self.calculate_agi()
        self.int = self.calculate_int()

    def calculate_str(self):
        strength = 4
        for i in range(1, self.lvl_p):
            if i < 20 and i % 2 != 0:
                strength += 2
            elif i % 2 == 0:
                strength += 3
            else:
                strength += 2
        return strength

    def calculate_agi(self):
        agility = 3
        for i in range(1, self.lvl_p):
            if i < 20 and i % 2 != 0:
                agility += 1
        return agility

    def calculate_int(self):
        intellect = 3
        for i in range(1, self.lvl_p):
            if i < 20 and i % 2 != 0:
                intellect += 2
            elif i % 2 == 0:
                intellect += 2
            else:
                intellect += 3
        return intellect
