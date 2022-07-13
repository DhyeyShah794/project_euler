from math import sqrt

"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

"""Answer is 6857"""

# My approach


def is_prime(num: int) -> bool:
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
        return True


def prime_factors_1(num: int) -> set:
    factors: list = []
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    for i in range(3, int(num/2) + 1, 2):
        if num % i == 0 and is_prime(i):
            factors.append(i)
            num //= i
    if num != 1 and is_prime(num):
        factors.append(num)
    return set(factors)


# More efficient approach (source: Wikipedia)


def prime_factors_2(num: int) -> set:
    factors: list = []
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    i: int = 3
    while i <= int(sqrt(num)) + 1:
        if num % i == 0:
            factors.append(i)
            num //= i
        else:
            i += 2
    if num != 1:
        factors.append(num)
    return set(factors)
