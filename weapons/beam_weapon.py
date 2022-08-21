from enum import Enum
from weapons.base_weapon import BaseWeapon
import json

class BeamWeapon(BaseWeapon):
    def __init__(self):
        self._maximum_power         = 0
        self._damage_modifier_1_min = 0
        self._damage_modifier_1_max = 0
        self._damage_modifier_2_min = 0
        self._damage_modifier_2_max = 0
        self._damage_modifier_3_min = 0
        self._damage_modifier_3_max = 0

    def get_maximum_power        (self): return self._maximum_power
    def get_damage_modifier_1_min(self): return self._damage_modifier_1_min
    def get_damage_modifier_1_max(self): return self._damage_modifier_1_max
    def get_damage_modifier_2_min(self): return self._damage_modifier_2_min
    def get_damage_modifier_2_max(self): return self._damage_modifier_2_max
    def get_damage_modifier_3_min(self): return self._damage_modifier_3_min
    def get_damage_modifier_3_max(self): return self._damage_modifier_3_max

    def set_maximum_power        (self, a): self._maximum_power = a
    def set_damage_modifier_1_min(self, a): self._damage_modifier_1_min = a
    def set_damage_modifier_1_max(self, a): self._damage_modifier_1_max = a
    def set_damage_modifier_2_min(self, a): self._damage_modifier_2_min = a
    def set_damage_modifier_2_max(self, a): self._damage_modifier_2_max = a
    def set_damage_modifier_3_min(self, a): self._damage_modifier_3_min = a
    def set_damage_modifier_3_max(self, a): self._damage_modifier_3_max = a


    def del_maximum_power        (self): del self._maximum_power
    def del_damage_modifier_1_min(self): del self._damage_modifier_1_min
    def del_damage_modifier_1_max(self): del self._damage_modifier_1_max
    def del_damage_modifier_2_min(self): del self._damage_modifier_2_min
    def del_damage_modifier_2_max(self): del self._damage_modifier_2_max
    def del_damage_modifier_3_min(self): del self._damage_modifier_3_min
    def del_damage_modifier_3_max(self): del self._damage_modifier_3_max

    maximum_power         = property(get_maximum_power        , set_maximum_power        , del_maximum_power        )
    damage_modifier_1_min = property(get_damage_modifier_1_min, set_damage_modifier_1_min, del_damage_modifier_1_min)
    damage_modifier_1_max = property(get_damage_modifier_1_max, set_damage_modifier_1_max, del_damage_modifier_1_max)
    damage_modifier_2_min = property(get_damage_modifier_2_min, set_damage_modifier_2_min, del_damage_modifier_2_min)
    damage_modifier_2_max = property(get_damage_modifier_2_max, set_damage_modifier_2_max, del_damage_modifier_2_max)
    damage_modifier_3_min = property(get_damage_modifier_3_min, set_damage_modifier_3_min, del_damage_modifier_3_min)
    damage_modifier_3_max = property(get_damage_modifier_3_max, set_damage_modifier_3_max, del_damage_modifier_3_max)
   
    def asDict(self):
        return self.__dict__

    def writeDict(self, dict):
        self.__dict__ = dict

    def __str__(self):
        s = "Weapon Type=BEAM\n" 
        s += "Weapon Model=" + str(self._weapon_model) + "\n"
        s += "Weapon Number=" + str(self._weapon_number) + "\n"
        s += "Firing Arcs FP=" + str(self._firing_arcs_fp) + "\n"
        s += "Firing Arcs F=" + str(self._firing_arcs_f) + "\n"
        s += "Firing Arcs FS=" + str(self._firing_arcs_fs) + "\n"
        s += "Firing Arcs AP=" + str(self._firing_arcs_ap) + "\n"
        s += "Firing Arcs A=" + str(self._firing_arcs_a) + "\n"
        s += "Firing Arcs AS=" + str(self._firing_arcs_as) + "\n"
        s += "Firing Chart=" + str(self._firing_chart) + "\n"
        s += "Maximum Power=" + str(self._maximum_power) + "\n"
        s += "Damage Modifier 1 Min=" + str(self._damage_modifier_1_min) + "\n"
        s += "Damage Modifier 1 Max=" + str(self._damage_modifier_1_max) + "\n"
        s += "Damage Modifier 2 Min=" + str(self._damage_modifier_2_min) + "\n"
        s += "Damage Modifier 2 Max=" + str(self._damage_modifier_2_max) + "\n"
        s += "Damage Modifier 3 Min=" + str(self._damage_modifier_3_min) + "\n"
        s += "Damage Modifier 3 Max=" + str(self._damage_modifier_3_max) + "\n"
        return s      


    def htmlStr(self):
        s = "Beam Weapon Type...................<b>" + str(self._weapon_model) + " (x" + str(self._weapon_number) + ")</b><br>"
        s+= "  Fore Firing Arcs.................<b>" + str(self._firing_arcs_fp) + " / " + \
                                                       str(self._firing_arcs_f) + " / " + \
                                                       str(self._firing_arcs_fs) + "</b><br>"
        s+= "  Aft Firing Arcs..................<b>" + str(self._firing_arcs_ap) + " / " + \
                                                       str(self._firing_arcs_a) + " / " + \
                                                       str(self._firing_arcs_as) + "</b><br>"
        s+= "  Firing Chart.....................<b>" + str(self._firing_chart) + "</b><br>"
        s+= "  Maximum Power....................<b>" + str(self._maximum_power) + "</b><br>"
        s+= "  Damage Modifiers" + "<br>"
        s+= "    +3.............................<b>" + str(self._damage_modifier_3_min) + "-" + str(self._damage_modifier_3_max) + "</b><br>"
        s+= "    +2.............................<b>" + str(self._damage_modifier_2_min) + "-" + str(self._damage_modifier_2_max) + "</b><br>"
        s+= "    +1.............................<b>" + str(self._damage_modifier_1_min) + "-" + str(self._damage_modifier_1_max) + "</b><br>"
        return s
