
class PrimeFactors:

    def generate(self, number):
        primes = []
        candidate = 2
        while number > 1:
            while number % candidate == 0:
                primes.append(candidate)
                number /= candidate
            candidate += 1

        return primes
