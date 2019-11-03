import pytest

from prime_factors import PrimeFactors


@pytest.fixture
def prime_factors():
    return PrimeFactors()


def test_one(prime_factors):
    assert [] == prime_factors.generate(1)


def test_two(prime_factors):
    assert [2] == prime_factors.generate(2)
