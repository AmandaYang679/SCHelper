from .weapon_infoblock.assault_rifle import Assault_rifle
from .medicine import Medicine


class MedicineAggregate:
    def __init__(self, infoblocks: Medicine):
        self.blocks = infoblocks
        # print(infoblocks.get_medicine_priority())
        
    def to_dict(self):
        # print(self.get_stamina_bonus())
        return {
            self.get_stamina_bonus()[0]: self.get_stamina_bonus()[1],
            self.get_medicine_priority()[0]: self.get_medicine_priority()[1],
            self.get_medicine_duration()[0]: self.get_medicine_duration()[1],
            self.get_medicine_hp_regen()[0]: self.get_medicine_hp_regen()[1],
            self.get_medicine_toxicity()[0]: self.get_medicine_toxicity()[1],
        }

    # def set_blocks(self, block: Medicine):
    #     self.block = block

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
    
    


class AssaultRifleAggregate:
    def __init__(self, infoblocks):
        self.blocks = infoblocks

    def set_blocks(self, block: Assault_rifle):
        self.blocks = block
        
    def get_max_durability(self):
        return self.blocks.get_max_durability()