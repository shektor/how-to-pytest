import pytest
from primes import is_prime
from primes import sum_of_primes


@pytest.mark.parametrize('number,result', [
    (1, False),
    (4, False),
    (15, False),
    (29, True),
    (83, True),
])
def test_is_prime(number, result):
    assert is_prime(number) == result


def test_sum_of_primes_empty_list():
    assert sum_of_primes([]) == 0
