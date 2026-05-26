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

    def get_all_items(self):
        return list(self.items.keys())

    def total_items(self):
        return sum(self.items.values())

    def find_item(self, query):
        return [name for name in self.items if query in name]

    def get_report(self):
        report = "=== Warehouse Report ===\n"
        for name, quantity in self.items.items():
            report += f"{name}: {quantity}\n"
        report += f"Total items: {self.total_items()}"
        return report

    def clear(self):
        self.items = {}
        self.history.append("CLEAR: warehouse cleared")
