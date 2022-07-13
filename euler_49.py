from math import sqrt
"""The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
 (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
 but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?"""

"""Answer is 296962999629"""

# Note that the difference between required primes is also 3330


def sieve(upper_bound: int) -> list:
    prime: list = [True] * (upper_bound + 1)
    prime[0] = prime[1] = False
    for p in range(3, int(sqrt(upper_bound)) + 1, 2):
        if prime[p]:
            for i in range(p * p, upper_bound + 1, p):
                prime[i] = False
        p += 2
    primes: list = [2]
    primes += [i for i in range(3, upper_bound + 1, 2) if prime[i]]
    return primes


def prime_check(num: int) -> bool:
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 6 != 1 and num % 6 != 5:
        return False
    else:
        for i in range(5, int(num ** 0.5) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False
        return True


def is_perm(numbers: tuple) -> bool:
    """This function accepts a tuple of numbers and checks if all of them are permutations of each other"""
    default = sorted(str(numbers[0]))
    for i in numbers:
        if sorted(str(i)) != default:
            return False
    return True


def req_primes(difference=3330):
    primes = sieve(10_000)[168:]  # Items before index 168 are not 4 digit numbers
    triples = []
    for i in primes:
        if prime_check(i + difference) and prime_check(i + 2 * difference):
            triples.append((i, i + difference, i + 2 * difference))
    req = [triple for triple in triples if is_perm(triple)]
    return str(req[1][0]) + str(req[1][1]) + str(req[1][2])
