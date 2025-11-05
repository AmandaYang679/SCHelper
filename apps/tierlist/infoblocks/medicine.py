from apps.tierlist.infoblocks.block.tooltip_medicine import TooltipMedicine


class Medicine:
    def parse(self, infoblocks: list):
        for block in infoblocks:
            # print(block, type(block))
            try:
                self.blocks.append(TooltipMedicine(block))
                
            except Exception as e:
                # print("error", e)
                pass
            

    def get_medicine_priority(self):
        for block in self.blocks:
            try:
                return block.get_medicine_priority()
            except:
                pass
            
            
    def get_stamina_bonus(self):
        for block in self.blocks:
            try:
                return block.get_stamina_bonus()
            except:
                pass
            
            
    def get_medicine_duration(self):
        for block in self.blocks:
            try:
                return block.get_medicine_duration()
            except:
                pass
            
            
    def get_medicine_hp_regen(self):
        for block in self.blocks:
            try:
                return block.get_medicine_hp_regen()
            except:
                pass
            
            
    def get_medicine_toxicity(self):
        for block in self.blocks:
            try:
                return block.get_medicine_toxicity()
            except:
                pass
            

    def __init__(self, infoblocks: list):
        self.blocks = []
        self.parse(infoblocks)
        # print(self.blocks)