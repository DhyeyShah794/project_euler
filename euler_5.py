from math import log, floor, sqrt
"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

"""Answer is 232792560"""

# My approach (semi-brute force approach, wimps out when the number of values exceed 120,000)
# Advantage: Doesn't need the numbers to start from 2 all the way to n. Numbers can be in any order and have any value


def gcd(num_1: int, num_2: int) -> int:
    """Use Euclidean algorithm to find the gcd of two numbers"""

    while num_1 % num_2 > 0:
        remainder: int = num_1 % num_2
        num_1, num_2 = num_2, remainder
    return num_2


def lcm_of_two_num(num_1: int, num_2: int) -> int:

    """Use the fact that lcm(a, b, c) = lcm(a, lcm(b, c)) and lcm(a, b) = (a * b)/gcd(a, b)
        Recursion works for small number of values"""

    return (num_1 * num_2)//gcd(num_1, num_2)


def lcm_general(numbers: list) -> int:
    result: int = 1
    for number in numbers:
        result: int = lcm_of_two_num(number, result)
    return result


# Other guy's approach (sieve not originally included) (works up to 1,000,000)


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


def minimum_multiple(n: int) -> int:
    """The highest power of a prime p less than n, n ∈ N is [log p(n)] and its value is p^[log p(n)].
    For natural numbers from 2 to n, the smallest positive number that is evenly divisible by all of the numbers is
    the product of the p^[log p(n)] ∀ p ∈ [2, n] where p is a prime number. """

    result: int = 1
    for i in sieve(n):
        result *= i ** floor(log(n, i))
    return result
