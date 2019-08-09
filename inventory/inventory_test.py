import pytest
from inventory import Inventory
from inventory import InvalidQuantityException
from inventory import NoSpaceException


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
    except (InvalidQuantityException, NoSpaceException) as raisedIssue:
        assert isinstance(raisedIssue, type(exception))
        assert raisedIssue.args == exception.args
    else:
        assert no_stock_inventory.total_items == 5
        assert no_stock_inventory.stocks[name]['price'] == price
        assert no_stock_inventory.stocks[name]['quantity'] == quantity
