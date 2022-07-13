import math
import fractions
import time
"""Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained."""

"""Answer is """

# First approach (brute force, will take over an hour to run)
def diophantine_solver(d: int, n: int):
    if d < 0 or math.sqrt(d).is_integer():
        return (0, 0)
    else:
        # for i in range(1, 500_000_000):
            # x = math.sqrt(n + d * i**2)
            # if x.is_integer() and x**2 - d * i**2 == n:
                # print(d, x, i)
                # return d, x
        i = 1
        while True:
            x = math.sqrt(n + d * i**2)
            if x.is_integer() and x**2 - d * i**2 == n:
                print(d, x)
                return d, x
            i += 1


# x_values = [diophantine_solver(num, 1) for num in range(2, 1001)]
# print(x_values)
# print(sorted(x_values))

# print(diophantine_solver(998, 1))


# Second approach

"""Find the fundamental solution by calculating the numerator and denominator of the continued fraction expansion of d"""


def cont_frac_expansion(r: int):
    if r == 1:
        return (1, 0)
    else:
        for i in range(1, 10):
            int_part = math.floor(r) 
            frac_part = '%.6f'%(r - int_part)
            r = fractions.Fraction(frac_part)
            print(int_part, r)

# start = time.time()
# print(cont_frac_expansion(3.245))
# print(time.time() - start)
