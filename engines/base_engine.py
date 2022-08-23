class BaseEngine(object):
    def __init__(self):
        self._engine_model  = ""
        self._power          = 0

    def get_engine_model (self): return self._engine_model
    def get_power        (self): return self._power

    def set_engine_model (self, a): self._engine_model = a
    def set_power        (self, a): self._power = a

    def del_engine_model (self): del self._engine_model
    def del_power        (self): del self._power

    engine_model  = property(get_engine_model, set_engine_model, del_engine_model )        
    power         = property(get_power,        set_power,        del_power        )
