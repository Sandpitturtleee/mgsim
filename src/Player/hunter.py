from abc import ABC

from src.Player.character import Character


class Hunter(Character, ABC):
    def __init__(self, lvl_p: int, lvl_e: int):
        super().__init__(lvl_p, lvl_e)
        self.str = self.calculate_str()
        self.agi = self.calculate_agi()
        self.int = self.calculate_int()

    def calculate_str(self):
        strength = 4
        for i in range(1,self.lvl_p):
            if i < 20:
                strength += 1
        return strength

    def calculate_agi(self):
        agility = 3
        for i in range(1, self.lvl_p):
            if i < 20:
                agility += 4
            else:
                agility += 5
        return agility

    def calculate_int(self):
        intellect = 3
        return intellect
