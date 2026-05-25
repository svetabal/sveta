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

def test_add_multiple_items():
    w = Warehouse()
    w.add_item("apple", 10)
    w.add_item("banana", 5)
    w.add_item("orange", 20)
    assert w.get_quantity("apple") == 10
    assert w.get_quantity("banana") == 5
    assert w.get_quantity("orange") == 20

def test_update_quantity():
    w = Warehouse()
    w.add_item("apple", 10)
    w.update_quantity("apple", 25)
    assert w.get_quantity("apple") == 25

def test_update_nonexistent_item():
    w = Warehouse()
    try:
        w.update_quantity("banana", 10)
        assert False
    except KeyError:
        assert True

def test_receive_items():
    w = Warehouse()
    w.add_item("apple", 10)
    w.receive_items("apple", 5)
    assert w.get_quantity("apple") == 15

def test_ship_items():
    w = Warehouse()
    w.add_item("apple", 10)
    w.ship_items("apple", 3)
    assert w.get_quantity("apple") == 7

def test_ship_more_than_available():
    w = Warehouse()
    w.add_item("apple", 10)
    try:
        w.ship_items("apple", 15)
        assert False
    except ValueError:
        assert True
