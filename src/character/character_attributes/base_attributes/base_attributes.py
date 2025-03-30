from src.character.character_attributes.base_attributes.lvl_attributes import LvlAttributes


class BaseAttributes:
    def __init__(self, character_lvl, enemy_lvl):
        ###### Atrybuty podstawowe #####
        # Profesja
        self.profession = self.__class__.__name__  # profesja
        # Poziom postaci
        self.lvl_attributes = LvlAttributes(character_lvl=character_lvl, enemy_lvl=enemy_lvl)
