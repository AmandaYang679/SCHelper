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


class ElementKeyValue():
    def parse(self, block: dict, element_key: str):
        name = block["key"]
        if name["key"] == element_key:
            v = block["value"]
            vv = v["lines"]
            self.value = vv["en"]
        else:
            raise Exception("Incorrect block type")


    def get_value(self):
        return self.value

    def __init__(self, block: dict, element_key: str):
        self.value = None
        self.parse(block, element_key)