"""2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?"""

"""Answer is 1366"""


def sum_digits_power(base: int, power: int) -> int:
    exact_power: int = base ** power
    digits: list = [int(i) for i in str(exact_power)]
    return sum(digits)
