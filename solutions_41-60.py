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


if __name__ == "__main__":
    start_time = time.time()
    print(problem_41())
    print("--- %s seconds ---" % (time.time() - start_time))
