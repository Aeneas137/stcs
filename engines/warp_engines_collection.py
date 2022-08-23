from engines.warp_engine import WarpEngine
import json

class WarpEnginesCollection(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(WarpEnginesCollection, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        if hasattr(self, 'loaded'):
            print("already loaded")
            return
        else:
            self.engine_file_name = "data/engines_warp.json"
            self.load_data()    

    def add_engine(self, engine):
        if not type(engine) == WarpEngine:
            print("Not a valid Warp Engine Object")
            return        
        self.EnginesDictionary[engine._engine_model] = engine

    def get_engine_by_model(self, model):
        if not model in self.EnginesDictionary:
            return None
        return self.EnginesDictionary[model]

    def load_data(self):
        self.EnginesDictionary = { }                                       # Reset the Dictionary of Engine
        print("Parsing Warp Engine file: " + self.engine_file_name + "...")
        try:
            with open(self.engine_file_name, "r") as read_file:
                data = json.load(read_file)                                # read and deserialize data
        
            for key in data:                                               # since the data is a dictionary
                eng = WarpEngine()                                             # for each entry
                eng.writeDict(data[key])                                   # create a engine, set the data
                self.add_engine(eng)                                       # Store the engine
                
        except Exception as ex:
            print("*** Error loading " + self.engine_file_name)
            print("*** " + str(ex))
            sys.exit()        
        
        self.loaded = 1
    def save_data(self):
        print("Saving Warp Engine Data: " + self.engine_file_name)

        vDict = { }
        for key in self.EnginesDictionary:                                 # you can only serialize primitives
            vDict[key] = self.EnginesDictionary[key].asDict()              # so convert your objects to dictionaries
     
        try:
            with open(self.engine_file_name, "w") as write_file:
                json.dump(vDict, write_file, indent=4)                     # write the json and make it pretty

        except Exception as ex:
            print("*** Error saving " + self.engine_file_name)
            print("*** " + str(ex))
            sys.exit()                        