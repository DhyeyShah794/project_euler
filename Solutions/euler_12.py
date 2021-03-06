from math import sqrt, ceil

"""The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?"""

"""Answer is 76576500"""


def triangle_num_gen(num_of_terms: int) -> list:
    """The difference between consecutive triangle numbers forms an A.P. with a = 2 and d = 1"""
    start_term: int = 1
    triangle_numbers: list = [1]
    for i in range(2, num_of_terms + 1):
        start_term += i
        triangle_numbers.append(start_term)
    return triangle_numbers


# First approach (semi-brute force, inefficient for numbers greater than 1024)


def factors(num: int) -> set:
    """Returns all divisors of a number"""
    all_factors: set = set()
    step: int = 2 if num % 2 else 1
    for i in range(1, ceil(sqrt(num)) + 1, step):
        if num % i == 0:
            all_factors.add(i), all_factors.add(num // i)
    return all_factors


def solution_1(min_num_of_factors: int) -> int:
    """The upper bound for number of divisors of a number n is 2√n
    Thus, the upper bound for a number with a minimum number of divisors is (num_of_divisors^2)/2"""
    triangle_numbers: list = triangle_num_gen((min_num_of_factors ** 2)//2)
    for number in triangle_numbers:
        if len(factors(number)) > min_num_of_factors:
            return number


# Project euler solution (comparatively faster)


def num_of_factors(num: int) -> int:
    """If n = p_1^a_1 * p_2^a_2 * p_3^a_3 * ... * p_n^a_n, where p_n is the nth prime,
    then the total number of factors of n = (a_1 + 1) * (a_2 + 1) * ... * (a_n + 1)
    This significantly reduces the time taken to calculate number of factors"""
    factors_of_num: list = []
    while num % 2 == 0:
        factors_of_num.append(2)
        num //= 2
    i: int = 3
    while i <= ceil(sqrt(num)) + 1:
        if num % i == 0:
            factors_of_num.append(i)
            num //= i
        else:
            i += 2
    if num != 1:
        factors_of_num.append(num)
    count: int = 1
    for i in set(factors_of_num):
        term: int = factors_of_num.count(i)
        count *= (term + 1)
    return count


def solution_2(min_num_of_factors: int) -> int:
    triangle_numbers: list = triangle_num_gen((min_num_of_factors ** 2)//2)
    for number in triangle_numbers:
        if num_of_factors(number) > min_num_of_factors:
            return number
