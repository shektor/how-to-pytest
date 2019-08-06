import math

def is_prime(num):
    if num < 2:
        return False

    num_sqrt = math.sqrt(num)
    sqrt_round_up = math.ceil(num_sqrt)

    for test_value in range(2, sqrt_round_up):
        quotient = num / test_value

        if quotient.is_integer():
            return False

    return True
