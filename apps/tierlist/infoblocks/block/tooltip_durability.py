# core.tooltip.info.durability
import json


class TooltipDurability:
    def parse(self):
        for elem in self.block["elements"]:
            try:
                elem_name = elem["name"]
                typee = elem_name["key"]
                # print(typee)
                if typee == "core.tooltip.info.durability":
                    v = elem["formatted"]
                    # print(elem_name["lines"])
                    self.name = elem_name["lines"]
                    self.value = v["value"]
                else:
                    raise Exception("Block is not durability")
            except:
                raise Exception("Incorrect block type")


    def get_durability(self):
        return (self.name, self.value)

    def __init__(self, block: dict):
        self.name = None
        self.value = None
        self.block = block
        self.parse()
