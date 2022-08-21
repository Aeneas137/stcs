class BaseWeapon(object):
    def __init__(self):
        self._weapon_model          = ""
        self._weapon_number         = 0
        self._firing_arcs_fp        = 0
        self._firing_arcs_f         = 0
        self._firing_arcs_fs        = 0
        self._firing_arcs_ap        = 0
        self._firing_arcs_a         = 0
        self._firing_arcs_as        = 0
        self._firing_chart          = ""

    def get_weapon_model         (self): return self._weapon_model
    def get_weapon_number        (self): return self._weapon_number
    def get_firing_arcs_fp       (self): return self._firing_arcs_fp
    def get_firing_arcs_f        (self): return self._firing_arcs_f
    def get_firing_arcs_fs       (self): return self._firing_arcs_fs
    def get_firing_arcs_ap       (self): return self._firing_arcs_ap
    def get_firing_arcs_a        (self): return self._firing_arcs_a
    def get_firing_arcs_as       (self): return self._firing_arcs_as
    def get_firing_chart         (self): return self._firing_chart

    def set_weapon_model         (self, a): self._weapon_model = a
    def set_weapon_number        (self, a): self._weapon_number = a
    def set_firing_arcs_fp       (self, a): self._firing_arcs_fp = a
    def set_firing_arcs_f        (self, a): self._firing_arcs_f = a
    def set_firing_arcs_fs       (self, a): self._firing_arcs_fs = a
    def set_firing_arcs_ap       (self, a): self._firing_arcs_ap = a
    def set_firing_arcs_a        (self, a): self._firing_arcs_a = a
    def set_firing_arcs_as       (self, a): self._firing_arcs_as = a
    def set_firing_chart         (self, a): self._firing_chart = a

    def del_weapon_model         (self): del self._weapon_model
    def del_weapon_number        (self): del self._weapon_number
    def del_firing_arcs_fp       (self): del self._firing_arcs_fp
    def del_firing_arcs_f        (self): del self._firing_arcs_f
    def del_firing_arcs_fs       (self): del self._firing_arcs_fs
    def del_firing_arcs_ap       (self): del self._firing_arcs_ap
    def del_firing_arcs_a        (self): del self._firing_arcs_a
    def del_firing_arcs_as       (self): del self._firing_arcs_as
    def del_firing_chart         (self): del self._firing_chart

    weapon_model          = property(get_weapon_model         , set_weapon_model         , del_weapon_model         )
    weapon_number         = property(get_weapon_number        , set_weapon_number        , del_weapon_number        )
    firing_arcs_fp        = property(get_firing_arcs_fp       , set_firing_arcs_fp       , del_firing_arcs_fp       )
    firing_arcs_f         = property(get_firing_arcs_f        , set_firing_arcs_f        , del_firing_arcs_f        )
    firing_arcs_fs        = property(get_firing_arcs_fs       , set_firing_arcs_fs       , del_firing_arcs_fs       )
    firing_arcs_ap        = property(get_firing_arcs_ap       , set_firing_arcs_ap       , del_firing_arcs_ap       )
    firing_arcs_a         = property(get_firing_arcs_a        , set_firing_arcs_a        , del_firing_arcs_a        )
    firing_arcs_as        = property(get_firing_arcs_as       , set_firing_arcs_as       , del_firing_arcs_as       )
    firing_chart          = property(get_firing_chart         , set_firing_chart         , del_firing_chart         )
