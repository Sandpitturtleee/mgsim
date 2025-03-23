from abc import ABC, abstractmethod
from src.Items.item import Item


class Weapons(Item, ABC):
    def __init__(
        self,
        lvl,
        player,
        damage_type,
        rarity_factor,
    ):
        super().__init__(lvl, player, damage_type, rarity_factor)
        self.damage_type = damage_type
        self.class_power = 1.00
        self.damage = self.calculate_damage()
        self.slow = self.calculate_slow()

    def calculate_damage(self):
        if len(self.weapon_factor[self.damage_type]) != 1:
            return 8 * self.weapon_factor[self.damage_type][0] * (
                self.rarity_power + self.lvl_power
            ), 8 * self.weapon_factor[self.damage_type][1] * (
                self.rarity_power + self.lvl_power
            )
        else:
            return (
                8
                * self.weapon_factor[self.damage_type][0]
                * (self.rarity_power + self.lvl_power)
            )

    def calculate_slow(self):
        if (
            "frost" in self.damage_type or "frost" in self.damage_type
        ) and "+" in self.damage_type:
            return self.slow_factor[self.damage_type.split("+", 1)[1]][0] * self.lvl
        elif (
            "frost" in self.damage_type or "frost" in self.damage_type
        ) and "+" not in self.damage_type:
            return self.slow_factor[self.damage_type][0] * self.lvl
        else:
            return 0
