from warehouse import Warehouse

def test_add_item():
    w = Warehouse()
    w.add_item("apple", 10)
    assert w.get_quantity("apple") == 10
