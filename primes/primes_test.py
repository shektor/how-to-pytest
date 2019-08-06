from primes import is_prime

def test_prime_low_number():
    assert is_prime(1) == False

def test_prime_prime_number():
    assert is_prime(29)

def test_prime_another_prime_number():
    assert is_prime(2)

def test_prime_a_third_prime_number():
    assert is_prime(83)

def test_prime_composite_number():
    assert is_prime(15) == False
