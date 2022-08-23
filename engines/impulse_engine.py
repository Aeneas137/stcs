from engines.base_engine import BaseEngine


class ImpulseEngine(BaseEngine):
    def asDict(self):
        return self.__dict__

    def writeDict(self, dict):
        self.__dict__ = dict

    def __str__(self):
        s = "Engine Type=Impulse\n" 
        s += "Power=" + str(self._power) + "\n"
        return s      


    def htmlStr(self):
        s = "Impulse Engine Type................<b>" + str(self.__engine_model) + "</b><br>"
        s+= "  Power Units Available............<b>" + str(self._power)
        return s
