from math import sqrt, ceil

"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

"""Answer is 31875000"""

# My approach (acceptable for numbers up to 2 * 10^7)


def triple_generator(max_value: int) -> list:
    """Generates all possible Pythagorean triples (primitive & non-primitive) where every triple member <= max_value
    Every primitive Pythagorean triple is of the form (m^2 - n^2, 2mn, m^2 + n^2) ∀ m, n ∈ N, m > n"""
    upper_bound: int = ceil(sqrt(max_value/2))
    triples: list = [(m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2) for m in range(1, upper_bound)
                     for n in range(1, upper_bound) if m > n]
    return triples


def product_of_triple(sum_of_num: int):
    """Finds the sum of all triples and returns the product of the corresponding triples element"""
    triples: list = triple_generator(sum_of_num)
    list_of_sums: list = [sum(i) for i in triples]
    try:
        req_triple: list = triples[list_of_sums.index(sum_of_num)]
    except ValueError:
        return None
    product: int = 1
    for i in req_triple:
        product *= i
    return product
