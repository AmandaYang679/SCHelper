from apps.tierlist.models import Item
from .weapon_infoblock.assault_rifle import Assault_rifle
from .medicine import Medicine


class MedicineAggregate:
    def __init__(self, item: Item):
        self.item = item
        self.blocks = None

    def set_blocks(self, block: Medicine):
        self.blocks = block

    def get_stamina_bonus(self):
        return self.blocks.get_stamina_bonus()
    
    def get_medicine_priority(self):
        return self.blocks.get_medicine_priority()
    
    def get_medicine_duration(self):
        return self.blocks.get_medicine_duration()
    
    def get_medicine_hp_regen(self):
        return self.blocks.get_medicine_hp_regen()
    
    def get_medicine_toxicity(self):
        return self.blocks.get_medicine_toxicity()

