"""Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal."""

"""Answer is 1533776805"""


def triangle_num_gen(num_of_terms: int) -> set:
    """The difference between consecutive triangle numbers forms an A.P. with a = 2 and d = 1"""
    start_term: int = 1
    triangle_numbers = set()
    triangle_numbers.add(1)
    for i in range(2, num_of_terms + 1):
        start_term += i
        triangle_numbers.add(start_term)
    return triangle_numbers


def pentagonal_num_gen(num_of_terms: int) -> set:
    start_term: int = 1
    pentagonal_numbers = set()
    pentagonal_numbers.add(1)
    for i in range(4, 3 * num_of_terms + 1, 3):  # Multiply by 3 since incrementing i by 3
        start_term += i
        pentagonal_numbers.add(start_term)
    return pentagonal_numbers


def hexagonal_num_gen(num_of_terms: int) -> set:
    start_term: int = 1
    hexagonal_numbers = set()
    hexagonal_numbers.add(1)
    for i in range(5, 4 * num_of_terms + 1, 4):
        start_term += i
        hexagonal_numbers.add(start_term)
    return hexagonal_numbers


def intersection_series(num_of_terms: int):  # Use an arbitrarily large value for num_of_terms
    triangle_numbers = triangle_num_gen(num_of_terms)
    pentagonal_numbers = pentagonal_num_gen(num_of_terms)
    hexagonal_numbers = hexagonal_num_gen(num_of_terms)
    intersection = set.intersection(triangle_numbers, pentagonal_numbers, hexagonal_numbers)
    return intersection
