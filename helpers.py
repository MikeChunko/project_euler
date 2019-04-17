# File name: solutions_21-40.py
# Author: Michael Chunko
# Date created: 1/5/19
# Python Version: 3.7

# This file contains some common helper algorithms used in solving various problem

import math


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


def number_rotations(n):
    """ Return the list of all circular rotations of the number n.
    Example: number_rotations(917) -> [917, 719, 197]. """
    current = str(n)
    result = []

    for i in range(0, len(current)):
        current = current[-1] + current[:-1]
        result.append(int(current))

    return result


def decimal_to_binary(n):
    """ Return a string representing the binary representation of the decimal number n.
        The resulting string does not contain any leading zeroes. """
    if n == 0:
        return "0"

    result = ""

    current_power = 1

    while current_power * 2 <= n:
        current_power *= 2

    while current_power >= 1:
        if n - current_power >= 0:
            n -= current_power
            result += "1"
        else:
            result += "0"

        current_power /= 2

    return result


def binary_to_decimal(s):
    """ Return an int representing a decimal representation of the binary number stored in the string s. """
    result = 0
    current_power = 1

    while s:
        if s[-1] == "1":
            result += current_power
        current_power *= 2
        s = s[:-1]

    return result


def is_palindrome(s):
    """ Return True if the string s is a palindrome.
        Return False otherwise. """
    while s:
        if s[0] != s[-1]:
            return False
        s = s[1:-1]

    return True


def is_coprime(a, b):
    """ Return True if the two numbers are coprime with each other.
        Return False otherwise.
        If either of the numbers are 1 or -1 they count as being coprime"""
    if math.gcd(a, b) == 1 or abs(a) == 1 or abs(b) == 1:
        return True
    return False


def fibonacci(n):
    """ Return a list of the first n Fibonacci numbers.
        n is assumed to be >= 2."""
    fibonacci_lst = [0, 1]

    for i in range(0, n - 2):
        fibonacci_lst.append(fibonacci_lst[-1] + fibonacci_lst[-2])

    return fibonacci_lst
