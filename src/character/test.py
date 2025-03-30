# from base_stats import BaseStats
#
#
# class Character:
#     def __init__(self, name: str, strength: int, agility: int, intellect: int, weapon_bonus: int, armor_bonus: int):
#         self.name = name
#
#         # Composition: Character contains BaseStats (which contains EquipmentStats)
#         self.base_stats = BaseStats(strength, agility, intellect, weapon_bonus, armor_bonus)
#
#     def __repr__(self):
#         return f"Character(name={self.name}, {self.base_stats})"
# 
#     from equipment_stats import EquipmentStats
#
#     class BaseStats:
#         def __init__(self, strength: int, agility: int, intellect: int, weapon_bonus: int, armor_bonus: int):
#             self.strength = strength
#             self.agility = agility
#             self.intellect = intellect
#
#             class EquipmentStats:
#                 def __init__(self, weapon_bonus: int, armor_bonus: int):
#                     self.weapon_bonus = weapon_bonus
#                     self.armor_bonus = armor_bonus
#
#                 def __repr__(self):
#                     return f"EquipmentStats(weapon_bonus={self.weapon_bonus}, armor_bonus={self.armor_bonus})"
#
#             # Composition: BaseStats contains EquipmentStats
#             self.equipment = EquipmentStats(weapon_bonus, armor_bonus)
#
#         @property
#         def total_strength(self):
#             return self.strength + self.equipment.weapon_bonus
#
#         @property
#         def total_agility(self):
#             return self.agility + self.equipment.armor_bonus
#
#         def __repr__(self):
#             return f"BaseStats(strength={self.strength}, agility={self.agility}, intellect={self.intellect}, {self.equipment})"
