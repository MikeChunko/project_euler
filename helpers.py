# File name: solutions_21-40.py
# Author: Michael Chunko
# Date created: 1/5/19
# Python Version: 3.7

# This file contains some common helper algorithms used in solving various problem

import math
import time
import sys


def eratosthenes_sieve(n):
    """ Return all prime numbers <= n using the Sieve of Eratosthenes. """
    primes = [1]
    possible_primes = list(range(2, n + 1))

    while possible_primes:
        primes += [possible_primes[0]]

        i = 0
        current_prime = primes[-1]
        while i < len(possible_primes):

            if possible_primes[i] % current_prime == 0:
                possible_primes.remove(possible_primes[i])
                i += current_prime - 1

            i += 1

    return primes
