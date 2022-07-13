from math import sqrt

"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

"""Answer is 142913828922"""

# My approach (Efficient for numbers up to 5 * 10^7)


def sum_primes_below(num: int) -> list:
    prime: list = [True] * (num + 1)
    prime[0] = prime[1] = False
    for p in range(3, int(sqrt(num)) + 1, 2):
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 2
    primes: list = [2]
    primes += [i for i in range(3, num + 1, 2) if prime[i]]
    return sum(primes)
