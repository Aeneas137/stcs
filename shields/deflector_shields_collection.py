from shields.deflector_shield import DeflectorShield
import json

class DeflectorShieldsCollection(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DeflectorShieldsCollection, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        if hasattr(self, 'loaded'):
            print("already loaded")
            return
        else:
            self.shield_file_name = "data/shields_deflector.json"
            self.load_data()

    def add_shield(self, shield):
        if not type(shield) == DeflectorShield:
            print("Not a valid Deflector Shield Object")
            return        
        self.ShieldDictionary[shield._shield_model] = shield

    def get_shield_by_model(self, model):
        if not model in self.ShieldDictionary:
            return None
        return self.ShieldDictionary[model]

    def load_data(self):
        self.ShieldDictionary = { }                                       # Reset the Dictionary of Engine
        print("Parsing Deflector Shield file: " + self.shield_file_name + "...")
        try:
            with open(self.shield_file_name, "r") as read_file:
                data = json.load(read_file)                                # read and deserialize data
        
            for key in data:                                               # since the data is a dictionary
                eng = DeflectorShield()                                             # for each entry
                eng.writeDict(data[key])                                   # create a engine, set the data
                self.add_shield(eng)                                       # Store the engine
                
        except Exception as ex:
            print("*** Error loading " + self.shield_file_name)
            print("*** " + str(ex))
            sys.exit()        
        
        self.loaded = 1
    def save_data(self):
        print("Saving Deflector Shield Data: " + self.shield_file_name)

        vDict = { }
        for key in self.ShieldDictionary:                                 # you can only serialize primitives
            vDict[key] = self.ShieldDictionary[key].asDict()              # so convert your objects to dictionaries
     
        try:
            with open(self.shield_file_name, "w") as write_file:
                json.dump(vDict, write_file, indent=4)                     # write the json and make it pretty

        except Exception as ex:
            print("*** Error saving " + self.shield_file_name)
            print("*** " + str(ex))
            sys.exit()                        