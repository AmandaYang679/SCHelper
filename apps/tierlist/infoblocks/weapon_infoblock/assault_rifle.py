import json
from apps.tierlist.infoblocks.block.tooltip_durability import TooltipDurability
from apps.tierlist.infoblocks.block.tooltip_medicine import TooltipMedicine


class Assault_rifle:
    def parse(self, infoblocks: list):
        for block in infoblocks:
            # print(block, type(block))
            try:
                self.blocks.append(TooltipMedicine(block))
                
            except Exception as e:
                # print("error", e)
                pass
            try:
                self.blocks.append(TooltipDurability(block))
            except Exception as e:
                # print("error", e)
                pass

    def __init__(self, infoblocks: list):
        self.blocks = []
        self.parse(infoblocks)
        # print(self.blocks)

    def get_absolute_damage(self):
        for block in self.blocks:
            try:
                return block.get_absolute_damage()
            except:
                pass

        raise Exception("assault rifle doesn't contain absolute damage")

    def get_durability(self):
        for block in self.blocks:
            try:
                return block.get_durability()
            except:
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
