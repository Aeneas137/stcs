"""
This is my code for testing the JSON serialization function

"""

import json
from weapon_collection import *
from weapon import *

class Specs(object):
    def __init__(self):
        self.classname = ""
        self.hulltype = ""

    def load(self,filename):
        #load from specs file
        print("Parsing file: " + filename + "...")

        with open(filename, "r") as read_file:
            data = json.load(read_file)

        self.classname = data["classname"]
        self.hulltype = data["hulltype"]
        
    def save(self,filename):
        #save to specs file
        print("Saving file: " + filename + "...")
        with open(filename, "w") as write_file:
            json.dump(self, write_file)

    def __str__(self):
        s = "classname=" + self.classname + "\n"
        s+= "hulltype=" + self.hulltype + "\n"
        return s
    

print("Test Code")
wepc = WeaponsCollection()

print(wepc.get_weapon_by_model("FH-11"))

# wep1 = Weapon()
# wep1.weapon_model = "FH-11"
# # print(wep1)

# wep2 = Weapon()
# wep2.weapon_model = "FH-5"
# # print(wep2)

# wep3 = Weapon()
# wep3.weapon_type = "MISSLE"
# wep3.weapon_model = "FP-4"
# # print(wep3)

# wepc.add_weapon(wep1)
# wepc.add_weapon(wep2)
# wepc.add_weapon(wep3)
# wepc.save_data()

