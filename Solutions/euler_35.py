from math import sqrt
"""The number 197 is called a circular prime because all rotations of the digits: 197, 971, and 719, are also prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""

"""Answer is 55"""


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


def all_rotations(num: int):
    rotations = []
    for i in range(0, len(str(num))):
        new_rotation = str(num)[i:] + str(num)[:i]
        rotations.append(int(new_rotation))
    return rotations


def num_of_circular_primes(upper_limit: int):
    primes = sieve(upper_limit)
    filter_1 = [i for i in primes if "2" not in str(i) and "5" not in str(i)]
    filter_2 = []
    for i in filter_1:
        possible_primes = all_rotations(i)
        for j in possible_primes:
            if not prime_check(j):
                break
        else:
            filter_2.append(i)
    filter_2 += [2, 5]  # 2 and 5 are ruled out in filter_1
    print(filter_2)
    return len(filter_2)
