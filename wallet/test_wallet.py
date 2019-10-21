from wallet import Wallet


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0
