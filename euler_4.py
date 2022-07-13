from itertools import combinations

"""A palindromic number reads the same both ways. The largest palindrome made from the product
 of two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of
  two 3-digit numbers."""

"""Answer is 906609"""

# Initial approach


def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]


def largest_palindrome_product_1(num_of_digits: int) -> int:
    start: int = 10 ** (num_of_digits - 1)
    end: int = (10 ** num_of_digits) - 1
    all_combinations: list = [(x, y) for x in range(end, start - 1, -1) for y in range(end, start - 1, -1)]
    products: list = [x*y for (x, y) in all_combinations]
    products.sort(reverse=True)
    for i in products:
        if is_palindrome(i):
            return i


# Second approach (the only difference is the use of itertools to generate all possible combinations)


def largest_palindrome_product_2(num_of_digits: int) -> int:
    start: int = 10 ** (num_of_digits - 1)
    end: int = (10 ** num_of_digits) - 1
    all_combinations = list(combinations([i for i in range(end, start - 1, -1)], 2))
    products: list = [x*y for (x, y) in all_combinations]
    palindromes: list = [i for i in products if is_palindrome(i)]
    return max(palindromes)
