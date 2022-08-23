class BaseShield(object):
    def __init__(self):
        self._shield_model          = ""

    def get_shield_model         (self): return self._shield_model
    def set_shield_model         (self, a): self._shield_model = a
    def del_shield_model         (self): del self._shield_model


    shield_model          = property(get_shield_model         , set_shield_model         , del_shield_model         )        