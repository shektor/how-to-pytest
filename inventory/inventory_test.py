import pytest
from inventory import Inventory
from inventory import InvalidQuantityException


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


def test_add_new_stock_success(no_stock_inventory):
    no_stock_inventory.add_new_stock('Test Jacket', 10.00, 5)

    assert no_stock_inventory.total_items == 5
    assert no_stock_inventory.stocks['Test Jacket']['price'] == 10.00
    assert no_stock_inventory.stocks['Test Jacket']['quantity'] == 5


@pytest.mark.parametrize('name, price, quantity, exception', [
    ('Test Jacket', 10.00, 0, InvalidQuantityException(
        'Cannot add a quantity of 0. All new stocks must have at least 1 item'))
])
def test_add_new_stock_bad_input(name, price, quantity, exception):
    inventory = Inventory(10)
    try:
        inventory.add_new_stock(name, price, quantity)
    except InvalidQuantityException as raisedIssue:
        assert isinstance(raisedIssue, type(exception))
        assert raisedIssue.args == exception.args
    else:
        pytest.fail("Expected error but found none")
