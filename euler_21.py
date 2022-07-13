from math import sqrt, ceil

"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, and a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
 The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

"""Answer is 31626"""

# Brute force approach (efficient for numbers less than 500,000)


def sum_proper_factors(num: int):
    """Returns all divisors of a number"""
    all_factors: list = [1]
    step: int = 2 if num % 2 else 1
    for i in range(1, ceil(sqrt(num)) + 1, step):
        if num % i == 0 and i != 1:
            all_factors.append(i), all_factors.append(num // i)
    return sum(set(all_factors))


def sum_amicable_pairs(upper_bound: int):
    sum_pairs = 0
    for i in range(2, upper_bound):
        temp = sum_proper_factors(i)
        if sum_proper_factors(temp) == i and i != sum_proper_factors(i):
            sum_pairs += i + sum_proper_factors(i)
    return sum_pairs//2  # Since one pair is counted twice
