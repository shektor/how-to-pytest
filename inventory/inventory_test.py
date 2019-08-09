import pytest
from inventory import Inventory, InvalidQuantityException, NoSpaceException, ItemNotFoundException


def test_default_inventory_initialisation():
    inventory = Inventory()

    assert inventory.limit == 100
    assert inventory.total_items == 0


def test_custom_inventory_limit():
    inventory = Inventory(25)

    assert inventory.limit == 25
    assert inventory.total_items == 0


@pytest.fixture
def no_stock_inventory():
    return Inventory(10)


@pytest.mark.parametrize('name, price, quantity, exception', [
    ('Test Jacket', 10.00, 0, InvalidQuantityException(
        'Cannot add a quantity of 0. All new stocks must have at least 1 item')),
    ('Test Jacket', 10.00, 25, NoSpaceException(
        'Cannot add these 25 items. Only 10 more items can be stored')),
    ('Test Jacket', 10.00, 5, None),
])
def test_add_new_stock(no_stock_inventory, name, price, quantity, exception):
    try:
        no_stock_inventory.add_new_stock(name, price, quantity)
    except (InvalidQuantityException, NoSpaceException) as raised_issue:
        assert isinstance(raised_issue, type(exception))
        assert raised_issue.args == exception.args
    else:
        assert no_stock_inventory.total_items == 5
        assert no_stock_inventory.stocks[name]['price'] == price
        assert no_stock_inventory.stocks[name]['quantity'] == quantity


@pytest.fixture
def ten_stock_inventory():
    inventory = Inventory(20)
    inventory.add_new_stock('Puma Duma', 100.00, 8)
    inventory.add_new_stock('Reebook', 25.50, 2)

    return inventory


@pytest.mark.parametrize('name, quantity, exception, new_quantity, new_total', [
    ('Puma Duma', 0,
        InvalidQuantityException(
            'Cannot remove a quantity of 0. Must remove at least 1 item'
        ),0, 0),
    ('Not Here', 5,
        ItemNotFoundException(
            'Could not find Not Here in our stocks. Cannot remove non-existing stock'
        ), 0, 0),
    ('Puma Duma', 25,
        InvalidQuantityException(
            'Cannot remove these 25 items. Only 8 items are in stock'
        ), 0, 0),
    ('Puma Duma', 5, None, 3, 5),
])
def test_remove_stock(ten_stock_inventory, name, quantity, exception, new_quantity, new_total):
    try:
        ten_stock_inventory.remove_stock(name, quantity)
    except (InvalidQuantityException, ItemNotFoundException) as raised_issue:
        assert isinstance(raised_issue, type(exception))
        assert raised_issue.args == exception.args
    else:
        assert ten_stock_inventory.total_items == new_total
        assert ten_stock_inventory.stocks[name]['quantity'] == new_quantity
