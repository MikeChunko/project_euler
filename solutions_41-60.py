# File name: solutions_41-60.py
# Author: Michael Chunko
# Date created: 6/7/19
# Python Version: 3.7

# This file contains the algorithms used for solving problems 21 through 40 (inclusive) from projecteuler.net

import math
import time
import helpers


def problem_41():
    """ Return the largest n-digit pandigital prime. """

    # We assume that a number can be at most 9-digit pandigital for this exercise.
    # Some simple math shows us that all 8- and 9-digit pandigital numbers are divisible by 3 and thus cannot be prime,
    # so we make our upperbound 7 digits
    primes = helpers.eratosthenes_sieve(7654321)

    while primes:
        if helpers.is_pandigital(primes[-1], len(str(primes[-1]))):
            return primes[-1]
        else:
            primes.remove(primes[-1])

    pass


def problem_45():
    """ Return the first triangle number (after 40755) that is also pentagonal and hexagonal.
        Triangle   T_n = n(n+1)/2
        Pentagonal P_n = n(3n-1)/2
        Hexagonal  H_n = n(2n-1) """

    # The n corresponding to T_n = 40755 can be found to be 285
    n = 285 + 1

    while True:
        T_n = (n * (n + 1)) // 2
        P_n = helpers.quadratic(3, -1, -T_n * 2)[1]
        if int(P_n) == P_n:
            H_n = helpers.quadratic(2, -1, -T_n)[1]
            if int(H_n) == H_n:
                return T_n
        n += 1


if __name__ == "__main__":
    start_time = time.time()
    print(problem_45())
    print("--- %s seconds ---" % (time.time() - start_time))
