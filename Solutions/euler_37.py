import time
from math import sqrt
"""The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""

"""Answer is 748317"""

def prime_check(num: int) -> bool:
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 6 != 1 and num % 6 != 5:
        return False
    else:
        for i in range(5, int(num ** 0.5) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False
        else:
            return True


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


def is_left_truncatable_prime(num: int):
    for i in range(0, len(str(num))):
        new_num = int(str(num)[i:])
        if prime_check(new_num):
            continue
        else:
            return False
    return True


def is_right_truncatable_prime(num: int):
    for i in range(-1, -len(str(num)), -1):
        new_num = int(str(num)[0: i])
        if prime_check(new_num):
            continue
        else:
            return False
    return True


def double_truncatable_primes(upper_bound: int):
    primes = sieve(upper_bound)
    filter_1 = [i for i in primes if int(str(i)[::-1]) % 2]  # Primes with even leading digit aren't right truncatable (except 23)
    required_primes = [i for i in filter_1 if is_left_truncatable_prime(i) and is_right_truncatable_prime(i)]
    required_primes.append(23)  # 23 is filtered out, it is the only false negative
    return sum(required_primes) - 15  # Question excludes 3, 5 and 7
