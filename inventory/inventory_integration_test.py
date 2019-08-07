from inventory import Inventory

def test_by_and_sell_nike_addidas():

    inventory = Inventory()
    assert inventory.limit == 100
    assert inventory.total_items == 0

    inventory.add_new_stock('Nike sneakers', 50.00, 10)
    assert inventory.total_items == 10

    inventory.add_new_stock('Addidas shirt', 70.00, 15)
    assert inventory.total_items == 25

    inventory.remove_stock('Nike sneakers', 2)
    assert inventory.total_items == 23

    inventory.remove_stock('Addidas shirt', 10)
    assert inventory.total_items == 13
