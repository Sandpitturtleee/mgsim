from abc import ABC
from src.character.character import Character


class Mage(Character, ABC):
    """
    A class representing a mage character class.
    Mag

    Attributes:
        character_lvl (int): Lvl of a character.
        enemy_lvl (int): Lvl of an enemy.
        character_attributes_lvl (dict): Attributes of a character
    """

    def __init__(self, character_lvl: int, enemy_lvl: int):
        super().__init__(character_lvl=character_lvl, enemy_lvl=enemy_lvl)
        self.character_attributes = self.calculate_attributes_lvl()

    def calculate_attributes_lvl(self) -> dict:
        """
        Calculates mage class character attributes.
        Nawigacja: Atrybuty Podstawowe -> Poziom postaci

        Returns:
            dict: Attributes.
        """
        strength = self.calculate_strength()
        agility = self.calculate_agility()
        intellect = self.calculate_intellect()
        return {"strength": strength, "agility": agility, "intellect": intellect}

    def calculate_strength(self) -> int:
        """
        Calculates strength attribute for a mage character class.

        Returns:
            int: Strength.
        """
        strength = 4
        for i in range(1, self.character_lvl):
            if i < 20:
                strength += 1
        return strength

    def calculate_agility(self) -> int:
        """
        Calculates agility attribute for a mage character class.

        Returns:
            int: Agility.
        """
        agility = 3
        for i in range(1, self.character_lvl):
            if i < 20:
                agility += 1
        return agility

    def calculate_intellect(self) -> int:
        """
        Calculates intellect attribute for a mage character class.

        Returns:
            int: Intellect.
        """
        intellect = 3
        for i in range(1, self.character_lvl):
            if i < 20:
                intellect += 3
            else:
                intellect += 5
        return intellect
