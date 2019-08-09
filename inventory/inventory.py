
class InvalidQuantityException(Exception):
    pass


class NoSpaceException(Exception):
    pass


class Inventory:
    def __init__(self, limit = 100):
        self.limit = limit
        self.total_items = 0
        self.stocks = {}


    def add_new_stock(self, item, price, quantity):
        if quantity <= 0:
            raise InvalidQuantityException(
                'Cannot add a quantity of {}. All new stocks must have at least 1 item'.format(quantity)
            )

        space_remaining = self.limit - self.total_items
        if quantity > space_remaining:
            raise NoSpaceException(
                'Cannot add these {} items. Only {} more items can be stored'.format(quantity, space_remaining)
            )

        self.total_items += quantity
        self.stocks[item] = { 'price': price, 'quantity': quantity }
