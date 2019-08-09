
class InvalidQuantityException(Exception):
    pass


class NoSpaceException(Exception):
    pass


class ItemNotFoundException(Exception):
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


    def remove_stock(self, name, quantity):
        if name not in self.stocks:
            raise ItemNotFoundException(
                'Could not find {} in our stocks. Cannot remove non-existing stock'.format(name)
            )

        if self.stocks[name]['quantity'] - quantity < 0:
            raise InvalidQuantityException(
                'Cannot remove these {} items. Only {} items are in stock'.format(quantity, self.stocks[name]['quantity'])
            )

        if quantity < 1:
            raise InvalidQuantityException(
                'Cannot remove a quantity of {}. Must remove at least 1 item'.format(quantity)
            )

        self.stocks[name]['quantity'] -= quantity
        self.total_items -= quantity
