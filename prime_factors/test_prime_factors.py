from prime_factors import PrimeFactors


def test_one():
    prime_factors = PrimeFactors()

    assert [] == prime_factors.generate(1)
