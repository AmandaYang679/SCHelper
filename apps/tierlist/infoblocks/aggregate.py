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
    
    def get_weight(self):
        return self.blocks.get_weight()
    
    def get_durability(self):
        return self.blocks.get_durability()
    
    def get_max_durability(self):
        return self.blocks.get_max_durability()
    
    def get_ammo_type(self):
        return self.blocks.get_ammo_type()
        
    def get_damage(self):
        return self.blocks.get_damage()
    
    def get_clip_size(self):
        return self.blocks.get_clip_size()
    
    def get_max_distance(self):
        return self.blocks.get_max_distance()
        
    def get_rate_of_fire(self):
        return self.blocks.get_rate_of_fire()
    
    def get_reload_time(self):
        return self.blocks.get_reload_time()
    
    def get_tactical_reload_time(self):
        return self.blocks.get_tactical_reload_time()
    
    def get_spread(self):
        return self.blocks.get_spread()
    
    def get_hip_fire_spread(self):
        return self.blocks.get_hip_fire_spread()
    
    def get_horizontal_recoil(self):
        return self.blocks.get_horizontal_recoil()
    
    def get_vertical_recoil(self):
        return self.blocks.get_vertical_recoil()
    
    def get_draw_time(self):
        return self.blocks.get_draw_time()
    
    def get_aiming_time(self):
        return self.blocks.get_aiming_time()
    
    def get_movement_speed(self):
        return self.blocks.get_movement_speed()
    