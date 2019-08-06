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
