from math import factorial
"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included."""

"""Answer is 40730"""


def is_sum_factorial_digits(num: int) -> bool:
    """Checks if the factorial value of a number is the same as the sum of the factorial of its digits"""
    digits: list = [int(char) for char in str(num)]
    return sum([factorial(digit) for digit in digits]) == num


def all_solutions():
    solutions = [i for i in range(1, 1_000_000) if is_sum_factorial_digits(i)]
    print(solutions)
    return sum(solutions) - 3  # 1 and 2 not included according to problem statement, so subtract their sum
