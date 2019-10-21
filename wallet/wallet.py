class Wallet:

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def add(self, amount):
        self.balance += amount

    def subtract(self, amount):
        if (self.balance - amount) < 0:
            raise InsufficientAmount('Insufficient balance'.format(amount))
        self.balance -= amount


class InsufficientAmount(Exception):
    pass
