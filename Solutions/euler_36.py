"""The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""

"""Answer is 872187"""


def decimal_to_binary(num):
    if type(num) != int:
        return TypeError
    elif num < 0:
        return ValueError
    else:
        return int(bin(num)[2:])


def is_palindrome(num: int):
    return str(num) == str(num)[::-1]


def sum_double_base_palindrome(upper_bound: int):
    palindromes = set(i for i in range(1, upper_bound, 2) if is_palindrome(i) and is_palindrome(decimal_to_binary(i)))
    print(palindromes)
    return sum(palindromes)
