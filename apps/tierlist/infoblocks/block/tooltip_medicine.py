# stalker.tooltip.medicine.info.priority
import json
from .element_numeric import ElementNumeric
from .element_key_value import ElementKeyValue


class TooltipMedicine:
    def parse(self):
        for elem in self.block["elements"]:
            if self.stamina_bonus == None:
                self.stamina_bonus = self.instance(elem["type"], "stalker.artefact_properties.factor.stamina_bonus", elem)
            if self.medicine_priority == None:
                self.medicine_priority = self.instance(elem["type"], "stalker.tooltip.medicine.info.priority", elem)
            if self.medicine_duration == None:
                self.medicine_duration = self.instance(elem["type"], "stalker.tooltip.medicine.info.duration", elem)
            if self.medicine_hp_regen == None:
                self.medicine_hp_regen = self.instance(elem["type"], "stalker.tooltip.medicine.info.hp_regen", elem)
            if self.medicine_toxicity == None:
                self.medicine_toxicity = self.instance(elem["type"], "stalker.tooltip.medicine.info.toxicity", elem)

    def get_stamina_bonus(self):
        return self.stamina_bonus.get_value()
    
    
    def get_medicine_priority(self):
        return self.medicine_priority.get_value()
    
    
    def get_medicine_duration(self):
        return self.medicine_duration.get_value()
    
    
    def get_medicine_hp_regen(self):
        return self.medicine_hp_regen.get_value()
    
    
    def get_medicine_toxicity(self):
        return self.medicine_toxicity.get_value()
    
    
    def instance(self, class_type, element_key, elem):
        try:
            if class_type == "numeric":
                return ElementNumeric(elem, element_key)
            elif class_type == "key-value":
                return ElementKeyValue(elem, element_key)
        except:
            pass

    

    def __init__(self, block: dict):
        self.stamina_bonus = None
        self.medicine_priority = None
        self.medicine_duration = None
        self.medicine_hp_regen = None
        self.medicine_toxicity = None
        self.block = block
        self.parse()