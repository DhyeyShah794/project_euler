"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

"""Answer is 837799"""


def collatz_chain_length(num: int) -> int:
    chain_length: int = 1
    while num != 1:
        if num % 2 == 0:
            num = num//2
        else:
            num = 3 * num + 1
        chain_length += 1
    return chain_length


# My approach


def largest_collatz_length_1(upper_bound: int) -> int:
    chain_lengths: list = [collatz_chain_length(i) for i in range(1, upper_bound)]
    return chain_lengths.index(max(chain_lengths)) + 1


# Project Euler approach (takes roughly half the time, can be further optimized using memoization)


def largest_collatz_length_2(upper_bound: int) -> int:
    """Collatz(2k) > Collatz(k) ∀ k ∈ N
    No need to check for numbers <= upper bound"""
    chain_lengths: list = [(collatz_chain_length(i)) for i in range(upper_bound//2, upper_bound)]
    value: int = max(chain_lengths)
    return chain_lengths.index(value) + upper_bound//2
