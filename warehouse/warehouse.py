class Warehouse:
    def __init__(self):
        self.items = {}
        self.history = []

    def add_item(self, name, quantity):
        self.items[name] = quantity
        self.history.append(f"ADD {name}: {quantity}")

    def get_quantity(self, name):
        return self.items[name]

    def update_quantity(self, name, quantity):
        if name not in self.items:
            raise KeyError(f"Item {name} not found")
        self.items[name] = quantity

    def receive_items(self, name, quantity):
        if name not in self.items:
            raise KeyError(f"Item {name} not found")
        self.items[name] += quantity
        self.history.append(f"RECEIVE {name}: +{quantity}")

    def ship_items(self, name, quantity):
        if name not in self.items:
            raise KeyError(f"Item {name} not found")
        if quantity > self.items[name]:
            raise ValueError("Not enough items in stock")
        self.items[name] -= quantity
        self.history.append(f"SHIP {name}: -{quantity}")

    def get_history(self):
        return self.history

    def test_history_content():
        w = Warehouse()
        w.add_item("apple", 10)
        w.receive_items("apple", 5)
        history = w.get_history()
        assert "ADD apple: 10" in history
        assert "RECEIVE apple: +5" in history

    def get_all_items(self):
        return list(self.items.keys())

    def total_items(self):
        return sum(self.items.values())

   def find_item(self, query):
        return [name for name in self.items if query in name]

    def find_item(self, query):
        return [name for name in self.items if query in name]
