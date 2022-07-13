"""The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000."""

"""Answer is 9110846700"""


def self_power(num: int) -> int:
    return num ** num


def digits_sum_powers(n: int) -> int:
    power_sum = sum([self_power(i) for i in range(1, n + 1)])
    return int(str(power_sum)[-10:])
