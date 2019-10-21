class Wallet:

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def add(self, amount):
        self.balance += amount

    def subtract(self, amount):
        self.balance -= amount
