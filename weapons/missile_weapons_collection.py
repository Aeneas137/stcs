from weapons.missile_weapon import MissileWeapon
import json


class MissileWeaponsCollection(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MissileWeaponsCollection, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        if hasattr(self, 'loaded'):
            print("already loaded")
            return
        else:
            self.weapon_file_name = "data/missile_weapons.json"
            self.load_data()
            
    def add_weapon(self, weapon):
        if not type(weapon) == MissileWeapon:
            print("Not a valid missle wepon Object")
            return        
        self.WeaponsDictionary[weapon._weapon_model] = weapon
    def get_weapon_by_model(self, model):
        if not model in self.WeaponsDictionary:
            return None
        return self.WeaponsDictionary[model]
        
    def load_data(self):
        self.WeaponsDictionary = { }                                       # Reset the Dictionary of Weapons
        print("Parsing Weapons file: " + self.weapon_file_name + "...")
        try:
            with open(self.weapon_file_name, "r") as read_file:
                data = json.load(read_file)                                # read and deserialize data
        
            for key in data:                                               # since the data is a dictionary
                wep = MissileWeapon()                                             # for each entry
                wep.writeDict(data[key])                                   # create a weapon, set the data
                self.add_weapon(wep)                                       # Store the weapon
                
        except Exception as ex:
            print("*** Error loading " + self.weapon_file_name)
            print("*** " + str(ex))
            sys.exit()        
        
        self.loaded = 1
    def save_data(self):
        print("Saving Weapons Data: " + self.weapon_file_name)

        vDict = { }
        for key in self.WeaponsDictionary:                                 # you can only serialize primitives
            vDict[key] = self.WeaponsDictionary[key].asDict()              # so convert your objects to dictionaries
     
        try:
            with open(self.weapon_file_name, "w") as write_file:
                json.dump(vDict, write_file, indent=4)                     # write the json and make it pretty

        except Exception as ex:
            print("*** Error saving " + self.weapon_file_name)
            print("*** " + str(ex))
            sys.exit()        