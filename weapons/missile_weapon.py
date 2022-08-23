from enum import Enum
from weapons.base_weapon import BaseWeapon
import json

class MissileWeapon(BaseWeapon):
    def __init__(self):
        self._power_to_arm          = 0
        self._damage                = 0        

    def get_power_to_arm         (self): return self._power_to_arm
    def get_damage               (self): return self._damage

    def set_power_to_arm         (self, a): self._power_to_arm = a
    def set_damage               (self, a): self._damage = a

    def del_power_to_arm         (self): del self._power_to_arm
    def del_damage               (self): del self._damage

    power_to_arm          = property(get_power_to_arm         , set_power_to_arm         , del_power_to_arm         )
    damage                = property(get_damage               , set_damage               , del_damage               )
   
    def asDict(self):
        return self.__dict__

    def writeDict(self, dict):
        self.__dict__ = dict

    def __str__(self):
        s = "Weapon Type=MISSLE\n" 
        s += "Weapon Model=" + str(self._weapon_model) + "\n"
        s += "Weapon Number=" + str(self._weapon_number) + "\n"
        s += "Firing Arcs FP=" + str(self._firing_arcs_fp) + "\n"
        s += "Firing Arcs F=" + str(self._firing_arcs_f) + "\n"
        s += "Firing Arcs FS=" + str(self._firing_arcs_fs) + "\n"
        s += "Firing Arcs AP=" + str(self._firing_arcs_ap) + "\n"
        s += "Firing Arcs A=" + str(self._firing_arcs_a) + "\n"
        s += "Firing Arcs AS=" + str(self._firing_arcs_as) + "\n"
        s += "Firing Chart=" + str(self._firing_chart) + "\n"
        s += "Power To Arm=" + str(self._power_to_arm) + "\n"
        s += "Damange=" + str(self._damage) + "\n"
        return s        

    def htmlStr(self):
        s = "Missile Weapon Type................<b>" + str(self._weapon_model) + " (x" + str(self._weapon_number) + ")</b><br>"
        s+= "  Fore Firing Arcs.................<b>" + str(self._firing_arcs_fp) + " / " + \
                                                       str(self._firing_arcs_f) + " / " + \
                                                       str(self._firing_arcs_fs) + "</b><br>"
        s+= "  Aft Firing Arcs..................<b>" + str(self._firing_arcs_ap) + " / " + \
                                                       str(self._firing_arcs_a) + " / " + \
                                                       str(self._firing_arcs_as) + "</b><br>"
        s+= "  Firing Chart.....................<b>" + str(self._firing_chart) + "</b><br>"
        s+= "  Power To Arm.....................<b>" + str(self._power_to_arm) + "</b><br>"
        s+= "  Damage...........................<b>" + str(self._damage) + "</b><br>"
        return s        
