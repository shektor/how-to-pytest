from wallet import Wallet


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0


def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100


def test_add_to_balance():
    wallet = Wallet()
    wallet.add(50)
    assert wallet.balance == 50


def test_subtract_from_balance():
    wallet = Wallet(10)
    wallet.subtract(5)
    assert wallet.balance == 5
