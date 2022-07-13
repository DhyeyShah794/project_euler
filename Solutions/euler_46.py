from math import sqrt
"""It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice
a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?"""

"""Answer is 5777"""


def sieve(upper_bound: int) -> list:
    prime: list = [True] * (upper_bound + 1)
    prime[0] = prime[1] = False
    for p in range(3, int(sqrt(upper_bound)) + 1, 2):
        if prime[p]:
            for i in range(p * p, upper_bound + 1, p):
                prime[i] = False
        p += 2
    primes: list = [2]
    primes += [i for i in range(3, upper_bound + 1, 2) if prime[i]]
    return primes


def odd_composites(upper_bound: int) -> list:
    """2x−1+4y(x+y) generates odd composite numbers
    Values for x and y are hardcoded here (minimized to reduce runtime, after finding the solution obviously)"""
    req = set(2*x-1+4*y*(x+y) for x in range(1, 50) for y in range(1, 50) if 2*x-1+4*y*(x+y) <= upper_bound)
    return sorted(req)


def satisfies_conjecture(upper_bound: int):
    composites = odd_composites(upper_bound)
    for composite in composites:
        primes = sieve(composite)  # Generated primes must be less than the composite number
        for prime in primes:
            result = sqrt((composite - prime)/2)
            if result.is_integer():
                # print(f"{composite} = {prime} + 2 * {int(result)} ^ 2")
                break
        else:
            return composite, False


# print(satisfies_conjecture(10000))
