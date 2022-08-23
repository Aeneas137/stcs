import json

from weapons.beam_weapons_collection import *
from weapons.missile_weapons_collection import *
from engines.impulse_engines_collection import *
from engines.warp_engines_collection import *
from shields.deflector_shields_collection import *

from weapons.beam_weapon import *
from weapons.missile_weapon import *
from engines.impulse_engine import *
from engines.warp_engine import *
from shields.deflector_shield import *

class Specs(object):
    def __init__(self):
        self.class_name = ""
        self.hull_type = ""
        self.superstructure = 0
        self.size_length = 0
        self.size_width = 0
        self.size_height = 0
        self.weight = 0
        self.crew = 0
        self.total_power = 0
        self.movement_ratio = ""
        self.defense_factor = 0
        self.weapon_damage_factor = 0
        self.combat_efficiency = 0        
        self.damage_chart = ""

        self.impulse_engine = None
        self.warp_engine = None
        self.deflector_shield = None
        self.beam_weapons = []
        self.missile_weapons = []

        self.top_image = ""
        self.side_image = ""
        self.centerx = 0
        self.centery = 0

    def load(self,filename):
        #load from specs file
        print("Parsing file: " + filename + "...")

        try:
            filepath = "data/shipspecs/" + filename
            with open(filepath, "r") as read_file:
                data = json.load(read_file)
            
        except Exception as ex:
            print("*** Error loading " + filename)
            print("*** " + str(ex))
            sys.exit()
            
        self.class_name = data["class_name"]
        self.hull_type = data["hull_type"]
        self.superstructure = data["superstructure"]
        self.size_length = data["size_length"]
        self.size_width = data["size_width"]
        self.size_height = data["size_height"]
        self.weight = data["weight"]
        self.crew = data["crew"]
        self.total_power = data["total_power"]
        self.movement_ratio = data["movement_ratio"]            
        self.defense_factor = data["defense_factor"]
        self.combat_efficiency = data["combat_efficiency"]
        self.weapon_damage_factor = data["weapon_damage_factor"]
        self.damage_chart = data["damage_chart"]

        if "deflector_shield" in data:
             v = data["deflector_shield"]
             dshc = DeflectorShieldsCollection()
             self.deflector_shield = dshc.get_shield_by_model(v)
        
        if "impulse_engine" in data:
             v = data["impulse_engine"]
             ienc = ImpulseEnginesCollection()
             self.impulse_engine = ienc.get_engine_by_model(v)

        if "warp_engine" in data:
             v = data["warp_engine"]
             wenc = WarpEnginesCollection()
             self.warp_engine = wenc.get_engine_by_model(v)
              
        if "beam_weapons" in data:
            beamc = BeamWeaponsCollection()
            for v in data["beam_weapons"]:
                beam = beamc.get_weapon_by_model(v)
                if beam == None:
                    break
                self.beam_weapons.append(beam)
        
        if "missile_weapons" in data:
            missilec = MissileWeaponsCollection()
            for v in data["missile_weapons"]:
                missile = missilec.get_weapon_by_model(v)
                if missile == None:
                    break
                self.missile_weapons.append(missile)      

        self.top_image = "images/" + data["top_image"]
        self.side_image = "images/" + data["side_image"]
        self.centerx = data["center"][0]
        self.centery = data["center"][1]
        
    def save(self,filename):
        #save to specs file
        print("Saving file: " + filename + "...")
        filepath = "data/shipspecs/" + filename
        with open(filepath, "w") as write_file:
            json.dump(self, write_file)

    def __str__(self):
        s = "class_name=" + self.class_name + "\n"
        s+= "hull_type=" + self.hull_type + "\n"
        return s

    def htmlStr(self):
        s = "Superstructure Points..............<b>" + str(self.superstructure) + "</b><br>"
        s+= "Damage Chart.......................<b>" + str(self.damage_chart) + "</b><br>"
        s+= "Length/Width/Height (meters).......<b>" + \
            str(self.size_length) + " / " + \
            str(self.size_width) + " / " + \
            str(self.size_height) + "</b><br>"
        s+= "Weight (metric tons)...............<b>" + str(self.weight) + "</b><br>"
        s+= "Crew...............................<b>" + str(self.crew) + "</b><br>"
        s+= "Total Power Units Available........<b>" + str(self.total_power) + "</b><br>"
        s+= "Movement Point Ratio...............<b>" + str(self.movement_ratio) + "</b><br>"

        if not self.warp_engine == None:            s += self.warp_engine.htmlStr()
        if not self.impulse_engine == None:         s += self.impulse_engine.htmlStr()           
        for beam in self.beam_weapons:              s += beam.htmlStr()
        for missile in self.missile_weapons:        s += missile.htmlStr()            
        if not self.deflector_shield == None:       s += self.deflector_shield.htmlStr()

        s+= "Defense Factor.....................<b>" + str(self.defense_factor) + "</b><br>"
        s+= "Weapon Damage Factor...............<b>" + str(self.weapon_damage_factor) + "</b><br>"
        s+= "Combat Efficiency..................<b>" + str(self.combat_efficiency) + "</b><br>"
        return s
    