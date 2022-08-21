from weapon import *
import json


class WeaponsCollection(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(WeaponsCollection, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if hasattr(self, 'loaded'):
            print("already loaded")
            return
        else:
            self.weapon_file_name = "weapons.json"
            self.load_data()
            

    def add_weapon(self, weapon):
        if not type(weapon) == Weapon:
            print("Not a valid wepon Object")
            return        
        self.WeaponsDictionary[weapon._weapon_model] = weapon

    def get_weapon_by_model(self, model):
        return self.WeaponsDictionary[model]
        
    def load_data(self):
        self.WeaponsDictionary = { }              # Dictionary of Weapons
        print("Parsing Weapons file: " + self.weapon_file_name + "...")
        try:
            with open(self.weapon_file_name, "r") as read_file:
                data = json.load(read_file)            
        
            for key in data:
                wep = Weapon()
                wep.writeDict(data[key])
                self.add_weapon(wep)
                
        except Exception as ex:
            print("*** Error loading " + self.weapon_file_name)
            print("*** " + str(ex))
            sys.exit()        
        
        self.loaded = 1

    def save_data(self):
        print("Saving Weapons Data: " + self.weapon_file_name)

        vDict = { }
        for key in self.WeaponsDictionary:
            vDict[key] = self.WeaponsDictionary[key].asDict()
     
        try:
            with open(self.weapon_file_name, "w") as write_file:
                json.dump(vDict, write_file, indent=4)

        except Exception as ex:
            print("*** Error saving " + self.weapon_file_name)
            print("*** " + str(ex))
            sys.exit()        