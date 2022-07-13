"""The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1, F2 = 1, F3 = 2, F4 = 3, F5 = 5, F6 = 8, F7 = 13, F8 = 21
F9 = 34, F10 = 55, F11 = 89, F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""

"""Answer is 4782"""

# My approaches (brute force)


def min_fibonacci_number_1(num_of_digits: int) -> int:
    """Returns the index of the first Fibonacci number with n digits"""
    a, b = 0, 1
    index = 0
    while len(str(a)) <= num_of_digits:
        if len(str(a)) == num_of_digits:
            return index
        a, b = b, a + b
        index += 1


def min_fibonacci_number_2(num_of_digits: int) -> int:  # Very slightly better than first function for larger values
    """Returns the index of the first Fibonacci number with n digits"""
    if num_of_digits == 0 or num_of_digits == 1:
        return 0
    a, b = 0, 1
    terms = []
    while len(str(a)) <= num_of_digits:
        terms.append(a)
        a, b = b, a + b

    req_terms = [(terms[i], i) for i in range(len(terms) - 1, len(terms)//2, -1) if len(str(terms[i])) == num_of_digits]
    return req_terms[-1][1]
