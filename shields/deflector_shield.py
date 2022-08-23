from shields.base_shield import BaseShield

class DeflectorShield(BaseShield):
    def __init__(self):
        self._point_ratio = [0, 0]
        self._maximum_power = 0
    
    def get_point_ratio           (self): return self._point_ratio
    def get_maximum_power         (self): return self._maximum_power

    def set_point_ratio           (self, a): self._point_ratio = a
    def set_maximum_power         (self, a): self._maximum_power = a

    def del_point_ratio           (self): del self._point_ratio
    def del_maximum_power         (self): del self._maximum_power

    point_ratio         = property(get_point_ratio,     set_point_ratio,     del_point_ratio)
    maximum_power       = property(get_maximum_power,   set_maximum_power,   del_maximum_power)

    def pointRatioStr(self):
        if len(self._point_ratio) < 2:
            return "Not Set correctly"
        return str(self._point_ratio[0]) + "/" + str(self._point_ratio[1])

    def asDict(self):
        return self.__dict__

    def writeDict(self, dict):
        self.__dict__ = dict

    def __str__(self):
        s = "Shield Type=Deflector\n" 
        s += "Point Ratio=" + self.pointRatioStr() + "\n"
        s += "Maximum Power=" + str(self._maximum_power) + "\n"
        return s      


    def htmlStr(self):
        s= "Deflector Shield Type..............<b>" + self._shield_model + "</b><br>"
        s+= "  Shield Point Ratio...............<b>" + self.pointRatioStr() + "</b><br>"
        s+= "  Maximum Shield Power.............<b>" + str(self._maximum_power) + "</b><br>"
        return s        