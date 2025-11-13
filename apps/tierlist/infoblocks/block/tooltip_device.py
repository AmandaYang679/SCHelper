from .element_numeric import ElementNumeric
from .element_key_value import ElementKeyValue


class TooltipDevice:
    def parse(self):
        for elem in self.block["elements"]:
            if self.weight == None:
                self.weight = self.instance(elem["type"], self._get_key("weight"), elem)
            if self.durability == None:
                self.durability = self.instance(elem["type"], self._get_key("durability"), elem)
            if self.max_durability == None:
                self.max_durability = self.instance(elem["type"], self._get_key("max_durability"), elem)
            if self.charge == None:
                self.charge = self.instance(elem["type"], self._get_key("charge"), elem)
            if self.passive_radius == None:
                self.passive_radius = self.instance(elem["type"], self._get_key("passive_radius"), elem)
            if self.active_radius == None:
                self.active_radius = self.instance(elem["type"], self._get_key("active_radius"), elem)
            if self.scan_angle == None:
                self.scan_angle = self.instance(elem["type"], self._get_key("scan_angle"), elem)

                
                
    def get_weight(self):
        return self.weight.get_value()
    
    
    def get_durability(self):
        return self.durability.get_value()
    
    
    def get_max_durability(self):
        return self.max_durability.get_value()
    
    
    def get_charge(self):
        return self.charge.get_value()
    
    
    def get_passive_radius(self):
        return self.passive_radius.get_value()
    
    
    def get_active_radius(self):
        return self.active_radius.get_value()
    
    
    def get_scan_angle(self):
        return self.scan_angle.get_value()
    
    
    
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
            "charge": {
                "name": "charge",
                "key": "stalker.gauge_meter_stat.metal_detector.info.charge",
            },
            "passive_radius": {
                "name": "passive_radius",
                "key": "stalker.gauge_meter_stat.metal_detector.info.passive_scan_radius",
            },
            "active_radius": {
                "name": "active_radius",
                "key": "stalker.gauge_meter_stat.metal_detector.info.active_scan_radius",
            },
            "scan_angle": {
                "name": "scan_angle",
                "key": "stalker.gauge_meter_stat.metal_detector.info.active_scan_angle",
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
        self.charge = None
        self.passive_radius = None
        self.active_radius = None
        self.scan_angle = None
        
        self.block = block
        self.parse()