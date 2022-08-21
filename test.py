"""
This is my code for testing the JSON serialization function

"""

import json
from weapons.beam_weapons_collection import *
from weapons.missile_weapons_collection import *
# from weapons.BeamWeapon import *  

print("Test Code")
wepc = BeamWeaponsCollection()
mwepc = MissileWeaponsCollection()

print(wepc.get_weapon_by_model("FH-11"))
print(mwepc.get_weapon_by_model("FP-4"))