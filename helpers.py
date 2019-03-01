# File name: solutions_21-40.py
# Author: Michael Chunko
# Date created: 1/5/19
# Python Version: 3.7

# This file contains some common helper algorithms used in solving various problem


def eratosthenes_sieve(n):
    """ Return all prime numbers <= n using the Sieve of Eratosthenes. """
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    primes = [1]
    for p in range(2, n):
        if prime[p]:
            primes += [p]

    return primes


def list_print(lst):
    """ Return a string containing lst represented in a nicer format. """
    result = ""

    for i in lst:
        for j in i:
            result += str(j) + "\t"
        result += "\n"

    return result
