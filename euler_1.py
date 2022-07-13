""""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
 The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000."""

"""Answer is 233168"""

# Brute force approach (For numbers up to 10^7)


def divisibility_check_3_or_5(n: int) -> bool:
    return n % 3 == 0 or n % 5 == 0


def num_div_by_3_and_5(upper_bound: int) -> int:
    return sum((i for i in range(1, upper_bound) if divisibility_check_3_or_5(i)))


# More efficient approach (works up to 10^154)


class SumMultiples:
    """Sn = [(a)(n)(n + 1)]/2
    First, find the sum of all multiples of 3, 5 and 15 up to that number.
    Then, subtract the sum of multiples of 15 as they have been counted twice."""
    def __init__(self, upper_bound):
        self.upper_bound = upper_bound

    def sum_3(self) -> float:
        self.upper_bound -= 1  # Range not inclusive
        last_term: int = self.upper_bound - self.upper_bound % 3
        number_of_terms: int = last_term // 3
        return (3/2) * number_of_terms * (number_of_terms + 1)

    def sum_5(self) -> float:
        self.upper_bound -= 1
        last_term: int = self.upper_bound - self.upper_bound % 5
        number_of_terms: int = last_term // 5
        return (5/2) * number_of_terms * (number_of_terms + 1)

    def sum_15(self) -> float:
        self.upper_bound -= 1
        last_term: int = self.upper_bound - self.upper_bound % 15
        number_of_terms: int = last_term // 15
        return (15/2) * number_of_terms * (number_of_terms + 1)

    def final_sum(self) -> float:
        return self.sum_3() + self.sum_5() - self.sum_15()
