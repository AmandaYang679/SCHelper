# {
#     "type": "key-value",
#     "key": {
#     "type": "translation",
#     "key": "core.tooltip.info.rank",
#     "args": {},
#     "lines": {
#         "ru": "Ранг",
#         "en": "Rank",
#         "es": "Rango",
#         "fr": "Rang"
#     }
#     },
#     "value": {
#     "type": "translation",
#     "key": "core.rank.master",
#     "args": {},
#     "lines": {
#         "ru": "Мастер",
#         "en": "Master",
#         "es": "Maestro",
#         "fr": "Maître"
#     }
#     }
# },

import json


class ElementKeyValue():
    def parse(self, block: dict, element_type: str):
        name = block["key"]
        if name["key"] == element_type:
            self.name = name["lines"]
            self.value = block["lines"]
        else:
            raise Exception("Incorrect block type")


    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value

    def __init__(self, block: dict, element_type: str):
        self.name = None
        self.value = None
        self.parse(block, element_type)