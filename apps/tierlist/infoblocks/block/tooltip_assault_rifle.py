from .element_numeric import ElementNumeric
from .element_key_value import ElementKeyValue


class TooltipAssaultRifle:
    def parse(self):
        for elem in self.block["elements"]:
            if self.weight == None:
                self.weight = self.instance(elem["type"], self._get_key("weight"), elem)
            if self.durability == None:
                self.durability = self.instance(elem["type"], self._get_key("durability"), elem)
            if self.max_durability == None:
                self.max_durability = self.instance(elem["type"], self._get_key("max_durability"), elem)
            if self.ammo_type == None:
                self.ammo_type = self.instance(elem["type"], self._get_key("ammo_type"), elem)
            if self.damage == None:
                self.damage = self.instance(elem["type"], self._get_key("damage"), elem)
            if self.clip_size == None:
                self.clip_size = self.instance(elem["type"], self._get_key("clip_size"), elem)
            if self.max_distance == None:
                self.max_distance = self.instance(elem["type"], self._get_key("max_distance"), elem)
            if self.rate_of_fire == None:
                self.rate_of_fire = self.instance(elem["type"], self._get_key("rate_of_fire"), elem)
            if self.reload_time == None:
                self.reload_time = self.instance(elem["type"], self._get_key("reload_time"), elem)
            if self.tactical_reload_time == None:
                self.tactical_reload_time = self.instance(elem["type"], self._get_key("tactical_reload_time"), elem)
            if self.spread == None:
                self.spread = self.instance(elem["type"], self._get_key("spread"), elem)
            if self.hip_spread == None:
                self.hip_spread = self.instance(elem["type"], self._get_key("hip_spread"), elem)
            if self.horizontal_recoil == None:
                self.horizontal_recoil = self.instance(elem["type"], self._get_key("horizontal_recoil"), elem)
            if self.vertical_recoil == None:
                self.vertical_recoil = self.instance(elem["type"], self._get_key("vertical_recoil"), elem)
            if self.draw_time == None:
                self.draw_time = self.instance(elem["type"], self._get_key("draw_time"), elem)
            if self.aiming_time == None:
                self.aiming_time = self.instance(elem["type"], self._get_key("aiming_time"), elem)
    
    
    def get_weight(self):
        return self.weight.get_value()
    
    
    def get_durability(self):
        return self.durability.get_value()
    
    
    def get_max_durability(self):
        return self.max_durability.get_value()
    
    
    def get_ammo_type(self):
        return self.ammo_type.get_value()


    def get_damage(self):
        return self.damage.get_value()
    
    
    def get_clip_size(self):
        return self.clip_size.get_value()
    
    
    def get_max_distance(self):
        return self.max_distance.get_value()


    def get_rate_of_fire(self):
        return self.rate_of_fire.get_value()
    
    
    def get_reload_time(self):
        return self.reload_time.get_value()
    
    
    def get_tactical_reload_time(self):
        return self.tactical_reload_time.get_value()
    
    
    def get_spread(self):
        return self.spread.get_value()
    
    
    def get_hip_fire_spread(self):
        return self.hip_spread.get_value()
    
    
    def get_horizontal_recoil(self):
        return self.horizontal_recoil.get_value()
    
    
    def get_vertical_recoil(self):
        return self.vertical_recoil.get_value()
    
    
    def get_draw_time(self):
        return self.draw_time.get_value()


    def get_aiming_time(self):
        return self.aiming_time.get_value()
    
    
    def _key_name_map(self):
        return {
            "weight": {
                "name": "weight",
                "key": "core.tooltip.info.weight",
            },
            "durability": {
                "name": "durability",
                "key": "core.tooltip.info.durability",
            },
            "max_durability": {
                "name": "max_durability",
                "key": "core.tooltip.info.max_durability",
            },
            "ammo_type": {
                "name": "ammo_type",
                "key": "weapon.tooltip.weapon.info.ammo_type",
            },
            "damage": {
                "name": "damage",
                "key": "core.tooltip.stat_name.damage_type.direct",
            },
            "clip_size": {
                "name": "clip_size",
                "key": "weapon.tooltip.weapon.info.clip_size",
            },
            "max_distance": {
                "name": "max_distance",
                "key": "weapon.tooltip.weapon.info.distance",
            },
            "rate_of_fire": {
                "name": "rate_of_fire",
                "key": "weapon.tooltip.weapon.info.rate_of_fire",
            },
            "reload_time": {
                "name": "reload_time",
                "key": "weapon.tooltip.magazine.info.reload_time",
            },
            "tactical_reload_time": {
                "name": "tactical_reload_time",
                "key": "weapon.tooltip.magazine.info.reload_time_tactical",
            },
            "spread": {
                "name": "spread",
                "key": "weapon.tooltip.weapon.info.spread",
            },
            "hip_spread": {
                "name": "hip_spread",
                "key": "weapon.tooltip.weapon.info.hip_spread",
            },
            "horizontal_recoil": {
                "name": "horizontal_recoil",
                "key": "weapon.tooltip.weapon.info.horizontal_recoil",
            },
            "vertical_recoil": {
                "name": "vertical_recoil",
                "key": "weapon.tooltip.weapon.info.recoil",
            },
            "draw_time": {
                "name": "draw_time",
                "key": "weapon.tooltip.weapon.info.draw_time",
            },
            "aiming_time": {
                "name": "aiming_time",
                "key": "weapon.tooltip.weapon.info.aim_switch",
            },
        }
    
    
    def _get_key(self, name):
        response = self._key_name_map()[name]
        return response["key"]

    
    def instance(self, class_type, element_key, elem):
        try:
            if class_type == "numeric":
                return ElementNumeric(elem, element_key)
            elif class_type == "key-value":
                return ElementKeyValue(elem, element_key)
        except:
            pass
        
        
    def __init__(self, block: dict):
        self.weight = None
        self.durability = None
        self.max_durability = None
        self.ammo_type = None
        self.damage = None
        self.clip_size = None
        self.max_distance = None
        self.rate_of_fire = None
        self.reload_time = None
        self.tactical_reload_time = None
        self.spread = None
        self.hip_spread = None
        self.horizontal_recoil = None
        self.vertical_recoil = None
        self.draw_time = None
        self.aiming_time = None
        
        self.block = block
        self.parse()
