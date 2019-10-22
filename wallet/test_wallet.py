import pytest

from wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()


@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 100'''
    return Wallet(100)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 100


def test_add_to_balance(empty_wallet):
    empty_wallet.add(50)
    assert empty_wallet.balance == 50


def test_subtract_from_balance(wallet):
    wallet.subtract(5)
    assert wallet.balance == 95


def test_subtract_raises_exception_on_insufficient_balance(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.subtract(100)


@pytest.mark.parametrize("earned, spent, expected", [
    (30, 10, 20),
    (20, 2, 18)
])
def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add(earned)
    my_wallet.subtract(spent)
    assert my_wallet.balance == expected
