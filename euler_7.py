from math import sqrt, log
"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?"""

"""Answer is 104743"""

# My approach (Uses sieve of Eratosthenes and finds the nth prime from that list, efficient for numbers up to 2 * 10^6)


def sieve(num: int) -> list:
    prime: list = [True] * (num + 1)
    prime[0] = prime[1] = False
    for p in range(3, int(sqrt(num)), 2):
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 2
    primes: list = [2]
    primes += [i for i in range(3, num + 1, 2) if prime[i]]
    return primes


def nth_prime(n: int) -> int:
    """n(ln(n) + ln(ln(n))) > p(n) > n(ln(n) + ln(ln(n)) − 1)"""
    upper_bound: float = n * (log(n) + log(log(n)))
    primes: list = sieve(int(upper_bound) + 1)
    return primes[n - 1]
