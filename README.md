# How to Pytest

Using the `pytest` testing framework and test-driven development to create prime number calculator and an inventory manager.

## Getting Started

```bash
> git clone git@github.com:shektor/how-to-pytest.git
> cd how-to-pytest

# It is generally recommended to install packages in a virtual environment but is optional
> python3 -m venv env
> . env/bin/activate

> pip install -r requirements.txt

# When finished using the program you can leave the virtual environment
> deactivate
```

## Running Tests

```bash
> pytest
```

## Usage

**Prime numbers**
```bash
# from /how-to-pytest
> cd primes
> python3

>>> from primes import is_prime
>>> is_prime(9)
False
>>> is_prime(2)
True
```

**Inventory manager**
```bash
# from /how-to-pytest
> cd inventory
> python3

>>> from inventory import Inventory, InvalidQuantityException, NoSpaceException, ItemNotFoundException
>>> inventory = Inventory(20)
>>> inventory.limit
20
>>> inventory.add_new_stock('Reebook', 25.50, 2)
>>> inventory.add_new_stock('Puma Duma', 100.00, 8)
>>> inventory.total_items
10
>>> inventory.remove_stock('Puma Duma', 20)
inventory.InvalidQuantityException: Cannot remove these 20 items. Only 8 items are in stock
>>> inventory.remove_stock('Puma Duma', 5)
>>> inventory.stocks
{'Reebook': {'price': 25.5, 'quantity': 2}, 'Puma Duma': {'price': 100.0, 'quantity': 3}}
>>> inventory.add_new_stock('Nikee', 0.50, 12)
inventory.NoSpaceException: Cannot add these 12 items. Only 10 more items can be stored
```
