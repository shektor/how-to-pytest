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
