from engines.base_engine import BaseEngine

class WarpEngine(BaseEngine):
    def __init__(self):
        self._number = 0
        self._stress_charts = ""
        self._maximum_speed = 0
        self._emergency_speed = 0

    def get_number                (self): return self._number
    def get_stress_charts         (self): return self._stress_charts
    def get_maximum_speed         (self): return self._maximum_speed
    def get_emergency_speed       (self): return self._emergency_speed

    def set_number                (self, a): self._number = a
    def set_stress_charts         (self, a): self._stress_charts = a
    def set_maximum_speed         (self, a): self._maximum_speed = a
    def set_emergency_speed       (self, a): self._emergency_speed = a

    def del_number                (self): del self._number
    def del_stress_charts         (self): del self._stress_charts
    def del_maximum_speed         (self): del self._maximum_speed
    def del_emergency_speed       (self): del self._emergency_speed

    number              = property(get_number,          set_number,          del_number)
    stress_chart        = property(get_stress_charts,   set_stress_charts,   del_stress_charts)
    maximum_speed       = property(get_maximum_speed,   set_maximum_speed,   del_maximum_speed)
    emergency_speed     = property(get_emergency_speed, set_emergency_speed, del_emergency_speed)

    def asDict(self):
        return self.__dict__

    def writeDict(self, dict):
        self.__dict__ = dict

    def __str__(self):
        s = "Engine Type=Warp\n" 
        s += "Power=" + str(self._power) + "\n"
        s += "Number=" + str(self._number) + "\n"
        s += "Engine Stress Charts=" + str(self._stress_charts) + "\n"
        s += "Maximum Speed=" + str(self._maximum_speed) + "\n"
        s += "Emergency Speed=" + str(self._emergency_speed) + "\n"
        return s      


    def htmlStr(self):
        s= "Warp Engine Type...................<b>" + \
            self._engine_model + \
            " (x" + str(self._number) + ")" + "</b><br>"
        s+= "  Power Units Available............<b>" + str(self._power) + "</b><br>"
        s+= "  Stress Charts....................<b>" + self._stress_charts + "</b><br>"
        s+= "  Maximum Safe Cruising Speed......<b>" + "Warp " + str(self._maximum_speed) + "</b><br>"
        s+= "  Emergency Speed..................<b>" + "Warp " + str(self._emergency_speed) + "</b><br>"
        return s    