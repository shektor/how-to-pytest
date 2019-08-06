import pytest
from primes import is_prime

@pytest.mark.parametrize('number,result', [
    (1, False),
    (15, False),
    (29, True),
    (83, True)
])
def test_is_prime(number, result):
    assert is_prime(number) == result
