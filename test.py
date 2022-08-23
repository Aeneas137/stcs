"""
This is my code for testing the JSON serialization function

"""

import json
from engines.impulse_engines_collection import *
from engines.warp_engines_collection import *
from shields.deflector_shields_collection import *

from engines.impulse_engine import *
from engines.warp_engine import *
from shields.deflector_shield import *

# from weapons.BeamWeapon import *  

print("Test Code")

iengc = ImpulseEnginesCollection()
wengc = WarpEnginesCollection()
dshlc = DeflectorShieldsCollection()

ieng = ImpulseEngine()
ieng.engine_model = "FIG-3"

weng = WarpEngine()
weng.engine_model = "FTWA"

dshl = DeflectorShield()
dshl.shield_model = "FSS"


iengc.add_engine(ieng)
wengc.add_engine(weng)
dshlc.add_shield(dshl)

iengc.save_data()
wengc.save_data()
dshlc.save_data()

