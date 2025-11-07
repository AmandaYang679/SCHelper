from apps.tierlist.infoblocks.block.tooltip_assault_rifle import TooltipAssaultRifle


class Assault_rifle:
    def parse(self, infoblocks: list):
        for block in infoblocks:
            try:
                self.blocks.append(TooltipAssaultRifle(block))
                
            except Exception as e:
                # print("error", e)
                pass
    
    
    def get_max_durability(self):
        for block in self.blocks:
            try:
                return block.get_max_durability()
            except:
                pass
            

    def __init__(self, infoblocks: list):
        self.blocks = []
        self.parse(infoblocks)
