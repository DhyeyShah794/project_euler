import itertools
import time

"""The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property."""

"""Answer is 16695334890"""


def pan_gen() -> list:
    perm = list(itertools.permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 10))
    new = [''.join(i) for i in perm]
    return new


def substr_check() -> list:
    pan_list = pan_gen()
    req = []
    for pan_num in pan_list:
        for i, num in zip(range(1, 9), [2, 3, 5, 7, 11, 13, 17]):
            if int(pan_num[i:i + 3]) % num != 0:
                break
        else:
            req.append(int(pan_num))
    return sum(req)


start = time.time()
print(substr_check())
print(time.time() - start)