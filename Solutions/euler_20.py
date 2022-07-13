"""n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""

"""Answer is 648"""


def factorial(num: int) -> int:
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product


def factorial_digit_sum(num: int) -> int:
    fac = factorial(num)
    digits = [int(i) for i in str(fac)]
    return sum(digits)


print(factorial_digit_sum(100))