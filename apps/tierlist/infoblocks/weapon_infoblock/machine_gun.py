from apps.tierlist.infoblocks.block.tooltip_machine_gun import TooltipMachineGun


class MachineGun:
    def parse(self, infoblocks: list):
        for block in infoblocks:
            try:
                self.blocks.append(TooltipMachineGun(block))
            except Exception as e:
                # print("error", e)
                pass
    
    
    def get_weight(self):
        for block in self.blocks:
            try:
                return block.get_weight()
            except:
                pass
            
            
    def get_durability(self):
        for block in self.blocks:
            try:
                return block.get_durability()
            except:
                pass
            
            
    def get_max_durability(self):
        for block in self.blocks:
            try:
                return block.get_max_durability()
            except:
                pass
            
            
    def get_movement_speed(self):
        for block in self.blocks:
            try:
                return block.get_movement_speed()
            except:
                pass
            
            
    def get_ammo_type(self):
        for block in self.blocks:
            try:
                return block.get_ammo_type()
            except:
                pass
            
            
    def get_damage(self):
        for block in self.blocks:
            try:
                return block.get_damage()
            except:
                pass
            
            
    def get_clip_size(self):
        for block in self.blocks:
            try:
                return block.get_clip_size()
            except:
                pass
            
            
    def get_max_distance(self):
        for block in self.blocks:
            try:
                return block.get_max_distance()
            except:
                pass
    
    
    def get_rate_of_fire(self):
        for block in self.blocks:
            try:
                return block.get_rate_of_fire()
            except:
                pass
            
            
    def get_reload_time(self):
        for block in self.blocks:
            try:
                return block.get_reload_time()
            except:
                pass
            
            
    def get_tactical_reload_time(self):
        for block in self.blocks:
            try:
                return block.get_tactical_reload_time()
            except:
                pass
            
            
    def get_reload_modifier(self):
        for block in self.blocks:
            try:
                return block.get_reload_modifier()
            except:
                pass
            
            
    def get_spread(self):
        for block in self.blocks:
            try:
                return block.get_spread()
            except:
                pass
            
            
    def get_hip_fire_spread(self):
        for block in self.blocks:
            try:
                return block.get_hip_fire_spread()
            except:
                pass
            
            
    def get_horizontal_recoil(self):
        for block in self.blocks:
            try:
                return block.get_horizontal_recoil()
            except:
                pass
            
            
    def get_vertical_recoil(self):
        for block in self.blocks:
            try:
                return block.get_vertical_recoil()
            except:
                pass
            
            
    def get_draw_time(self):
        for block in self.blocks:
            try:
                return block.get_draw_time()
            except:
                pass
            
            
    def get_aiming_time(self):
        for block in self.blocks:
            try:
                return block.get_aiming_time()
            except:
                pass
            
            
    def get_movement_speed(self):
        for block in self.blocks:
            try:
                return block.get_movement_speed()
            except:
                pass
            
            
    def __init__(self, infoblocks: list):
        self.blocks = []
        self.parse(infoblocks)