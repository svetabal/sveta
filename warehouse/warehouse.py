class Warehouse:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        self.items[name] = quantity

    def get_quantity(self, name):
        return self.items[name]

    def update_quantity(self, name, quantity):
        if name not in self.items:
            raise KeyError(f"Item {name} not found")
        self.items[name] = quantity
