from enum import Enum
import json

# class WeaponTypeEnum(Enum):
#     BEAM = 1
#     MISSLE = 2

class Weapon(object):
    def __init__(self):
        self._weapon_type           = "BEAM"                     # BEAM or MISSLE
        self._weapon_model          = ""
        self._weapon_number         = 0
        self._firing_arcs_fp        = 0
        self._firing_arcs_f         = 0
        self._firing_arcs_fs        = 0
        self._firing_arcs_ap        = 0
        self._firing_arcs_a         = 0
        self._firing_arcs_as        = 0
        self._firing_chart          = ""
        self._maximum_power         = 0
        self._power_to_arm          = 0
        self._damage                = 0        
        self._damage_modifier_1_min = 0
        self._damage_modifier_1_max = 0
        self._damage_modifier_2_min = 0
        self._damage_modifier_2_max = 0
        self._damage_modifier_3_min = 0
        self._damage_modifier_3_max = 0

    def get_weapon_type          (self): return self._weapon_type
    def get_weapon_model         (self): return self._weapon_model
    def get_weapon_number        (self): return self._weapon_number
    def get_firing_arcs_fp       (self): return self._firing_arcs_fp
    def get_firing_arcs_f        (self): return self._firing_arcs_f
    def get_firing_arcs_fs       (self): return self._firing_arcs_fs
    def get_firing_arcs_ap       (self): return self._firing_arcs_ap
    def get_firing_arcs_a        (self): return self._firing_arcs_a
    def get_firing_arcs_as       (self): return self._firing_arcs_as
    def get_firing_chart         (self): return self._firing_chart
    def get_maximum_power        (self): return self._maximum_power
    def get_power_to_arm         (self): return self._power_to_arm
    def get_damage               (self): return self._damage
    def get_damage_modifier_1_min(self): return self._damage_modifier_1_min
    def get_damage_modifier_1_max(self): return self._damage_modifier_1_max
    def get_damage_modifier_2_min(self): return self._damage_modifier_2_min
    def get_damage_modifier_2_max(self): return self._damage_modifier_2_max
    def get_damage_modifier_3_min(self): return self._damage_modifier_3_min
    def get_damage_modifier_3_max(self): return self._damage_modifier_3_max

    def set_weapon_type          (self, a): self._weapon_type = a
    def set_weapon_model         (self, a): self._weapon_model = a
    def set_weapon_number        (self, a): self._weapon_number = a
    def set_firing_arcs_fp       (self, a): self._firing_arcs_fp = a
    def set_firing_arcs_f        (self, a): self._firing_arcs_f = a
    def set_firing_arcs_fs       (self, a): self._firing_arcs_fs = a
    def set_firing_arcs_ap       (self, a): self._firing_arcs_ap = a
    def set_firing_arcs_a        (self, a): self._firing_arcs_a = a
    def set_firing_arcs_as       (self, a): self._firing_arcs_as = a
    def set_firing_chart         (self, a): self._firing_chart = a
    def set_maximum_power        (self, a): self._maximum_power = a
    def set_power_to_arm         (self, a): self._power_to_arm = a
    def set_damage               (self, a): self._damage = a
    def set_damage_modifier_1_min(self, a): self._damage_modifier_1_min = a
    def set_damage_modifier_1_max(self, a): self._damage_modifier_1_max = a
    def set_damage_modifier_2_min(self, a): self._damage_modifier_2_min = a
    def set_damage_modifier_2_max(self, a): self._damage_modifier_2_max = a
    def set_damage_modifier_3_min(self, a): self._damage_modifier_3_min = a
    def set_damage_modifier_3_max(self, a): self._damage_modifier_3_max = a


    def del_weapon_type          (self): del self._weapon_type
    def del_weapon_model         (self): del self._weapon_model
    def del_weapon_number        (self): del self._weapon_number
    def del_firing_arcs_fp       (self): del self._firing_arcs_fp
    def del_firing_arcs_f        (self): del self._firing_arcs_f
    def del_firing_arcs_fs       (self): del self._firing_arcs_fs
    def del_firing_arcs_ap       (self): del self._firing_arcs_ap
    def del_firing_arcs_a        (self): del self._firing_arcs_a
    def del_firing_arcs_as       (self): del self._firing_arcs_as
    def del_firing_chart         (self): del self._firing_chart
    def del_maximum_power        (self): del self._maximum_power
    def del_power_to_arm         (self): del self._power_to_arm
    def del_damage               (self): del self._damage
    def del_damage_modifier_1_min(self): del self._damage_modifier_1_min
    def del_damage_modifier_1_max(self): del self._damage_modifier_1_max
    def del_damage_modifier_2_min(self): del self._damage_modifier_2_min
    def del_damage_modifier_2_max(self): del self._damage_modifier_2_max
    def del_damage_modifier_3_min(self): del self._damage_modifier_3_min
    def del_damage_modifier_3_max(self): del self._damage_modifier_3_max

    weapon_type           = property(get_weapon_type          , set_weapon_type          , del_weapon_type          )
    weapon_model          = property(get_weapon_model         , set_weapon_model         , del_weapon_model         )
    weapon_number         = property(get_weapon_number        , set_weapon_number        , del_weapon_number        )
    firing_arcs_fp        = property(get_firing_arcs_fp       , set_firing_arcs_fp       , del_firing_arcs_fp       )
    firing_arcs_f         = property(get_firing_arcs_f        , set_firing_arcs_f        , del_firing_arcs_f        )
    firing_arcs_fs        = property(get_firing_arcs_fs       , set_firing_arcs_fs       , del_firing_arcs_fs       )
    firing_arcs_ap        = property(get_firing_arcs_ap       , set_firing_arcs_ap       , del_firing_arcs_ap       )
    firing_arcs_a         = property(get_firing_arcs_a        , set_firing_arcs_a        , del_firing_arcs_a        )
    firing_arcs_as        = property(get_firing_arcs_as       , set_firing_arcs_as       , del_firing_arcs_as       )
    firing_chart          = property(get_firing_chart         , set_firing_chart         , del_firing_chart         )
    maximum_power         = property(get_maximum_power        , set_maximum_power        , del_maximum_power        )
    power_to_arm          = property(get_power_to_arm         , set_power_to_arm         , del_power_to_arm         )
    damage                = property(get_damage               , set_damage               , del_damage               )
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
        s = "Weapon Type=" + str(self._weapon_type) + "\n"
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
        s += "Power To Arm=" + str(self._power_to_arm) + "\n"
        s += "Damange=" + str(self._damage) + "\n"
        s += "Damage Modifier 1 Min=" + str(self._damage_modifier_1_min) + "\n"
        s += "Damage Modifier 1 Max=" + str(self._damage_modifier_1_max) + "\n"
        s += "Damage Modifier 2 Min=" + str(self._damage_modifier_2_min) + "\n"
        s += "Damage Modifier 2 Max=" + str(self._damage_modifier_2_max) + "\n"
        s += "Damage Modifier 3 Min=" + str(self._damage_modifier_3_min) + "\n"
        s += "Damage Modifier 3 Max=" + str(self._damage_modifier_3_max) + "\n"
        return s        
