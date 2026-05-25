from warehouse import Warehouse

def test_add_item():
    w = Warehouse()
    w.add_item("apple", 10)
    assert w.get_quantity("apple") == 10

def test_get_nonexistent_item():
    w = Warehouse()
    try:
        w.get_quantity("banana")
        assert False
    except KeyError:
        assert True
