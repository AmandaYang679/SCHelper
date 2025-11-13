from apps.tierlist.infoblocks.block.tooltip_device import TooltipDevice


class Device:
    def parse(self, infoblocks: list):
        for block in infoblocks:
            try:
                self.blocks.append(TooltipDevice(block))
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
            
            
    def get_charge(self):
        for block in self.blocks:
            try:
                return block.get_charge()
            except:
                pass
            
            
    def get_passive_radius(self):
        for block in self.blocks:
            try:
                return block.get_passive_radius()
            except:
                pass
            
            
    def get_active_radius(self):
        for block in self.blocks:
            try:
                return block.get_active_radius()
            except:
                pass
            
            
    def get_scan_angle(self):
        for block in self.blocks:
            try:
                return block.get_scan_angle()
            except:
                pass
            
    
    def __init__(self, infoblocks: list):
        self.blocks = []
        self.parse(infoblocks)