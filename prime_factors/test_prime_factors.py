import pytest

from prime_factors import PrimeFactors


@pytest.fixture
def prime_factors():
    return PrimeFactors()


def test_one(prime_factors):
    assert prime_factors.generate(1) == []


def test_two(prime_factors):
    assert prime_factors.generate(2) == [2]


def test_three(prime_factors):
    assert prime_factors.generate(3) == [3]


def test_four(prime_factors):
    assert prime_factors.generate(4) == [2, 2]
