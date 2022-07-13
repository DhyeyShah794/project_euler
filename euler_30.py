"""Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""

"""Answer is 443839"""


def is_sum_digit_powers(num: int, power: int) -> bool:
    digits: list = [char for char in str(num)]
    return sum([pow(int(digit), power) for digit in digits]) == num


def sum_all_solutions(power: int):
    solutions = [i for i in range(1, 1_000_000) if is_sum_digit_powers(i, power)]
    return sum(solutions) - 1  # Since 1 is not counted as a solution


# print(sum_all_solutions(5))
