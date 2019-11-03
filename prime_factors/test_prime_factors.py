from prime_factors import PrimeFactors


def test_one():
    prime_factors = PrimeFactors()

    assert [] == prime_factors.generate(1)


def test_two():
    prime_factors = PrimeFactors()

    assert [2] == prime_factors.generate(2)