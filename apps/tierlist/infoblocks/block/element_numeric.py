# {
#     "type": "numeric",
#     "name": {
#     "type": "translation",
#     "key": "core.tooltip.info.weight",
#     "args": {},
#     "lines": {
#         "ru": "Вес",
#         "en": "Weight",
#         "es": "Peso",
#         "fr": "Poids"
#     }
#     },
#     "value": 0.075,
#     "formatted": {
#     "value": {
#         "ru": "0,08 кг",
#         "en": "0.08 kg",
#         "es": "0,08 kg",
#         "fr": "0,08 kg"
#     },
#     "nameColor": "838383",
#     "valueColor": "838383"
#     }
# }

# stalker.tooltip.medicine.info.priority
import json


class ElementNumeric():
    def parse(self, block: dict, element_key: str):
        name = block["name"]
        if name["key"] == element_key:
            self.value = block["value"]
        else:
            raise Exception("Incorrect block type")
    
    def get_value(self):
        return self.value

    def __init__(self, block: dict, element_key: str):
        self.value = None
        self.parse(block, element_key)
