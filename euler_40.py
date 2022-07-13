"""An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""

"""Answer is 210"""


def num_generator() -> str:
    decimal_part = ""
    for i in range(1, 500_000):
        decimal_part += str(i)
    return "." + decimal_part


def value():
    num: str = num_generator()
    product = 1
    for i in range(1, 7):
        product *= int(num[10 ** i])
    return product
