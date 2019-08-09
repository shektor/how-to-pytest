
class Inventory:
    def __init__(self, limit = 100):
        self.limit = limit
        self.total_items = 0
        self.stocks = {}


    def add_new_stock(self, item, price, quantity):
        self.total_items += quantity
        self.stocks[item] = { 'price': price, 'quantity': quantity }
