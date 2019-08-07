from inventory import Inventory


def test_default_inventory_initialisation():
    inventory = Inventory()

    assert inventory.limit == 100
    assert inventory.total_items == 0


def test_custom_inventory_limit():
    inventory = Inventory(25)

    assert inventory.limit == 25
    assert inventory.total_items == 0
