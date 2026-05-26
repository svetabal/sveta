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

def test_history():
    w = Warehouse()
    w.add_item("apple", 10)
    w.receive_items("apple", 5)
    w.ship_items("apple", 3)
    history = w.get_history()
    assert len(history) == 3

def test_history_content():
    w = Warehouse()
    w.add_item("apple", 10)
    w.receive_items("apple", 5)
    history = w.get_history()
    assert "ADD apple: 10" in history
    assert "RECEIVE apple: +5" in history

def test_get_all_items():
    w = Warehouse()
    w.add_item("apple", 10)
    w.add_item("banana", 5)
    items = w.get_all_items()
    assert "apple" in items
    assert "banana" in items

def test_total_items():
    w = Warehouse()
    w.add_item("apple", 10)
    w.add_item("banana", 5)
    assert w.total_items() == 15

def test_find_item():
    w = Warehouse()
    w.add_item("apple", 10)
    w.add_item("banana", 5)
    assert w.find_item("app") == ["apple"]
    assert w.find_item("an") == ["banana"]

def test_get_report():
    w = Warehouse()
    w.add_item("apple", 10)
    w.add_item("banana", 5)
    report = w.get_report()
    assert "apple" in report
    assert "banana" in report
    assert "10" in report
    assert "5" in report

def test_clear_warehouse():
    w = Warehouse()
    w.add_item("apple", 10)
    w.add_item("banana", 5)
    w.clear()
    assert w.total_items() == 0
    assert w.get_all_items() == []
