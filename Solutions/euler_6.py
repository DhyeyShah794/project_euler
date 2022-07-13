"""The sum of the squares of the first ten natural numbers is 385.

The square of the sum of the first ten natural numbers is 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
3025 - 385 = 2640.

Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum. """

"""Answer is 25164150"""

# My approach
# Efficient for numbers up to 10^100,000


class Difference:
    def __init__(self, n: int):
        self.n = n

    def sum_of_squares(self) -> int:
        """1^2 + 2^2 + 3^2 + ... + n^2 = n(n + 1)(2n + 1)/6"""
        return self.n * (self.n + 1) * (2 * self.n + 1)//6

    def square_of_sum(self) -> int:
        """(1 + 2 + 3 + ... + n)^2 = (n(n + 1)/2)^2"""
        return (self.n * (self.n + 1) // 2) ** 2

    def difference(self) -> int:
        return self.square_of_sum() - self.sum_of_squares()


# Other guy's approach (Reduces the number of operations, marginally faster)


def difference(n: int) -> int:
    """Difference = [n(n + 1)(2n + 1)/6] - [n(n + 1)/2]^2
    Can be further simplified to n(n + 1)(3n^2 - n + 2)/12"""
    return n * (n + 1) * (3 * n + 2) * (n - 1)//12
