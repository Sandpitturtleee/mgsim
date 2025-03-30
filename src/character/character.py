import numpy as numpy
from abc import ABC, abstractmethod

from src.character.character_attributes.base_attributes.base_attributes import BaseAttributes


# TODO check character stats with in-game data for all professions
class Character(ABC):
    def __init__(self, character_lvl: int, enemy_lvl: int):
        self.character_lvl = character_lvl
        self.enemy_lvl = enemy_lvl
        # ###### Atrybuty podstawowe #####
        self.base_attributes = BaseAttributes(character_lvl=character_lvl, enemy_lvl=enemy_lvl)

        #Placeholder example
        self.lvl_attributes = self.base_attributes.lvl_attributes  # Shortcut to LvlAttributes
        print(f"Character Level: {self.lvl_attributes.character_attributes_lvl}")

        # # Siła
        # self.hp_gain_strength = self.calculate_hp_gain_strength()  # hp z siły
        # self.hp_gain_armor_strength = (
        #     self.calculate_hp_gain_armor_strength()
        # )  # hp z zbrojki
        # self.hp_bon_strength = self.calculate_hp_bon_strength()  # hp z umek
        # self.crit_val_gain_strength = (
        #     self.calculate_crit_val_gain_strength()
        # )  # siła kryta fiz
        # self.dmg_gain_strength = self.calculate_dmg_gain_strength()  # wzrost dmg z siły
        # # Intelekt
        # self.absorb_limit_intellect = (
        #     self.calculate_absorb_limit_intellect()
        # )  # limit punktów absorbcji
        # self.crit_m_val_gain_intellect = (
        #     self.calculate_crit_m_val_gain_intellect()
        # )  # siła kryta mag
        # self.mana_intellect = self.calculate_mana_intellect()  # mana
        # self.dmg_gain_intellect = (
        #     self.calculate_dmg_gain_intellect()
        # )  # wzrost dmg z intelektu
        # # Zręcznosc
        # self.sa_agility = self.calculate_sa_agility()  # sa z zrecznosci
        # self.evade_gain_agility = (
        #     self.calculate_evade_gain_agility()
        # )  # unik z zrecznosci
        # self.dmg_gain_agility = (
        #     self.calculate_dmg_gain_agility()
        # )  # wzrost dmg z zrecznosci
        #
        # # Zycie
        # self.hp = 20  # bazowe hp
        # # Szybkość ataku
        # self.at = self.calculate_at()  # szybkosc ataku do tur
        # # Obniżanie szybkości ataku przeciwnika
        # self.slow = 0  # TODO z eqwipunku umki
        # # Spowolnienie
        # self.poison0 = 0  # TODO z eqwipunku umki
        # self.of_poison0 = 0  # TODO z eqwipunku umki
        # self.frost0 = 0  # TODO z eqwipunku umki
        # # Leczenie
        # self.heal = 0  # TODO z eqwipunku umki
        # # Energia
        # self.energy = 0  # TODO z eqwipunku umki
        # # Mana
        # self.mana = 0  # TODO z eqwipunku umki
        # # Siła ciosu krytycznego
        # self.crit_val = (
        #     120 + self.crit_val_gain_lvl + self.crit_val_gain_strength
        # )  # TODO z eqwipunku umki
        # self.crit_m_val_fire = (
        #     120 + self.crit_val_gain_lvl + self.crit_m_val_gain_intellect
        # )  # TODO z eqwipunku umki
        # self.crit_m_val_frost = (
        #     120 + self.crit_val_gain_lvl + self.crit_m_val_gain_intellect
        # )  # TODO z eqwipunku umki
        # self.crit_m_val_light = (
        #     120 + self.crit_val_gain_lvl + self.crit_m_val_gain_intellect
        # )  # TODO z eqwipunku umki
        # self.of_crit_val = (
        #     120 + self.crit_val_gain_lvl + self.crit_val_gain_strength
        # )  # TODO z eqwipunku umki

        ###### Typy redukcji obrażen #####
        # Pancerz
        self.armor = 0
        # Odpornosc na żywioły
        self.res_fire = 0
        self.res_frost = 0
        self.res_light = 0
        # Odpornosc na trucizne
        self.act = 0
        # Odpornosc na głęboką ranę
        self.wound_red = 0
        # Absorbcja
        self.absorb = 0
        # Absorbcja magiczna
        self.absorb_m = 0

        ###### Obniżanie statystyk przeciwnika #####
        # Niszczenie pancerza
        self.ac_dmg = 0
        # Niszczenie odpornosci
        self.ac_m_dmg = 0
        # Niszczenie absorbcji
        self.abs_dest = 0
        # Obniżanie uniku
        self.low_evade = 0
        # Obniżanie szansy na cios krytyczny przeciwnika
        self.low_crit = 0
        # Szansa na zniszczenie energii przeciwnikowi
        self.en_fatigue = 0
        # Szansa na zniszczenie many przeciwnikowi
        self.mana_fatigue = 0

        ###### Regularne zdarzenia losowe #####
        # Cios krytyczny
        self.crit = 0
        self.of_crit = 0
        # Przebicie pancerza
        self.pierce = 0
        # Głęboka rana
        self.wound0 = 0
        self.of_wound0 = 0
        # Unik
        self.evade = 0
        # Blok
        self.block = 0
        # Blok przebicia
        self.pierce_b = 0
        # Kontra
        self.contra = 0
        # Stun
        self.stun = 0
        # TODO wszystko wyżej

    def calculate_hp_gain_strength(self):
        return self.base_attributes.lvl_attributes.character_attributes_lvl * 5

    def calculate_hp_gain_armor_strength(self):
        # TODO with items
        return 0

    def calculate_hp_bon_strength(self):
        # TODO with skills
        return 0

    def calculate_crit_val_gain_strength(self):
        return self.character_attributes_lvl["strength"] / (
            0.5 * min(self.character_lvl, 300)
        )

    def calculate_dmg_gain_strength(self):
        # TODO with skills
        return 0

    def calculate_absorb_limit_intellect(self):
        return self.character_attributes_lvl["intellect"] * 7

    def calculate_crit_m_val_gain_intellect(self):
        return self.character_attributes_lvl["intellect"] / (
            0.5 * min(self.character_lvl, 300)
        )

    def calculate_mana_intellect(self):
        # TODO with skills
        return 0

    def calculate_dmg_gain_intellect(self):
        # TODO with skills
        return 0

    def calculate_sa_agility(self):
        return min(2, 0.02 * self.character_attributes_lvl["agility"]) + max(
            0, 0.002 * (self.character_attributes_lvl["agility"] - 100)
        )

    def calculate_evade_gain_agility(self):
        return self.character_attributes_lvl["agility"] / 30

    def calculate_dmg_gain_agility(self):
        # TODO with skills
        return 0

    def calculate_at(self):
        return 1 / (self.sa_agility + 1)
