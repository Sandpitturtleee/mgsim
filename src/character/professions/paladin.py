from abc import ABC
from src.character.character import Character


class Paladin(Character, ABC):
    """
    A class representing a paladin character class.
    Paladyn

    Attributes:
        character_lvl (int): Lvl of a character.
        enemy_lvl (int): Lvl of an enemy.
        character_attributes (dict): Attributes of a character
    """

    def __init__(self, character_lvl: int, enemy_lvl: int):
        super().__init__(character_lvl=character_lvl, enemy_lvl=enemy_lvl)
        self.character_attributes_lvl = self.calculate_attributes_lvl()

    def calculate_attributes_lvl(self) -> dict:
        """
        Calculates warrior class character attributes.
        Nawigacja: Atrybuty Podstawowe -> Poziom postaci

        Returns:
            dict: Attributes.
        """
        strength = self.calculate_strength()
        agility = self.calculate_agility()
        intellect = self.calculate_intellect()
        return {"strength": strength, "agility": agility,"intellect": intellect}

    def calculate_strength(self) -> int:
        """
        Calculates strength attribute for a paladin character class.

        Returns:
            int: Strength.
        """
        strength = 4
        for i in range(1, self.character_lvl):
            if i < 20 and i % 2 != 0:
                strength += 2
            elif i % 2 == 0:
                strength += 3
            else:
                strength += 2
        return strength

    def calculate_agility(self) -> int:
        """
        Calculates agility attribute for a paladin character class.

        Returns:
            int: Agility.
        """
        agility = 3
        for i in range(1, self.character_lvl):
            if i < 20 and i % 2 != 0:
                agility += 1
        return agility

    def calculate_intellect(self) -> int:
        """
        Calculates intellect attribute for a paladin character class.

        Returns:
            int: Intellect.
        """
        intellect = 3
        for i in range(1, self.character_lvl):
            if i < 20 and i % 2 != 0:
                intellect += 2
            elif i % 2 == 0:
                intellect += 2
            else:
                intellect += 3
        return intellect
