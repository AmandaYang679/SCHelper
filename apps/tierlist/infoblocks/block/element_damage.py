class ElementDamage():
    def parse(self, block: dict):
        for _, v in block.items():
            self.value.append(v)
    
    def get_value(self):
        return self.value[:-1]

    def __init__(self, block: dict):
        self.value = []
        self.parse(block)