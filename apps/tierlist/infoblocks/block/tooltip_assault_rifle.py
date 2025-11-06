from .element_numeric import ElementNumeric
from .element_key_value import ElementKeyValue


class TooltipAssaultRifle:
    def parse(self):
        for elem in self.block["elements"]:
            if self.max_durability == None:
                self.max_durability = self.instance(elem["type"], "core.tooltip.info.max_durability", elem)


    def get_durability(self):
        return (self.max_durability.get_name(), self.max_durability.get_value())

    
    def instance(self, class_type, element_key, elem):
        try:
            if class_type == "numeric":
                return ElementNumeric(elem, element_key)
            elif class_type == "key-value":
                return ElementKeyValue(elem, element_key)
        except:
            pass
        
        
    def __init__(self, block: dict):
        self.max_durability = None
        self.block = block
        self.parse()
