import pytest

from prime_factors import PrimeFactors


@pytest.fixture
def prime_factors():
    return PrimeFactors()


@pytest.mark.parametrize("number, prime_factors_list", [
    (1, []),
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (6, [2, 3]),
    (8, [2, 2, 2]),
    (9, [3, 3]),
    (12, [2, 2, 3]),
    (90, [2, 3, 3, 5]),
    (147, [3, 7, 7]),
    (330, [2, 3, 5, 11])
])
def test_generate(prime_factors, number, prime_factors_list):
    assert prime_factors.generate(number) == prime_factors_list
