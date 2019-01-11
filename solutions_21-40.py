# File name: solutions_21-40.py
# Author: Michael Chunko
# Date created: 1/5/19
# Python Version: 3.7

# This file contains the algorithms used for solving problems 21 through 40 (inclusive) from projecteuler.net

import math
import time
import sys


def problem_21(n):
    """ Return the sum of all the amicable numbers under n.
        An amicable number is part of a pair of numbers, a and b, where a != b, d(a) = b, and d(b) = a.
        d(n) is defined as the sum of all proper divisors of n"""
    proper_divisors = {1: 0, 2: 1}  # Takes the format (i, d(i))

    # Find d(i) and add it to proper_divisors
    for i in range(3, n):
        divisor_sum = 1
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                divisor_sum += j

        proper_divisors[i] = divisor_sum

    amicable_sum = 0
    print(proper_divisors)

    # Find the sum of the amicable numbers
    for key in proper_divisors:
        # This checks, essentially, to see if there is an amicable number for key and that this amicable number
        # is not equal to itself.
        if proper_divisors[key] != -1 and proper_divisors[key] in proper_divisors \
                and proper_divisors[proper_divisors[key]] == key and key != proper_divisors[key]:
            amicable_sum += proper_divisors[key] + key
            print(key, proper_divisors[key], amicable_sum)
            proper_divisors[key] = -1

    return amicable_sum


def problem_22(n):
    """ Return the sum of all the name scores in the file n.
        The name score is defined as the sum of the alphabetical values for each letter in the name
        multiplied by its alphabetical position. """
    file = open(n, "r")
    name_list = file.read().split(",")
    file.close()

    # Remove the extra double quotes surrounding each name
    for i in range(0, len(name_list)):
        name_list[i] = name_list[i][1:-1]

    name_list.sort()

    name_scores = [0] * len(name_list)
    for i in range(0, len(name_list)):
        for char in name_list[i]:
            name_scores[i] += ord(char) - 64

        name_scores[i] *= i + 1

    return sum(name_scores)


def problem_23():
    """ Return the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
        An abundant number is one whose proper divisors add up to be greater than itself.
        It is known that all integers greater than 28123 can be written as the sum of two abundant numbers.
        This function works, just not remotely fast. """

    def is_abundant(n):
        """ Return True if n is abundant. """
        divisor_sum = 1
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                divisor_sum += i

        return divisor_sum > n

    abundant_numbers = [i for i in range(1, 28123) if is_abundant(i)]

    sums = 0
    # It is known that the first abundant number is 12
    for i in range(12, 28123 + 1):
        for j in abundant_numbers:
            if j > i:
                sums += i
                print("GOTCHA")
                break
            if j - i in abundant_numbers:
                break
            print(i)

    return sums


def problem_24(n):
    """ Return the nth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        A lexicographic permutation is one where the list of all permutations is sorted numerically/alphabetically"""
    elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def all_permutations(elements):
        """ Return a list of all possible permutations of elements, with each permutation expressed as a list. """
        if len(elements) <= 1:
            yield elements
        else:
            for i in range(0, len(elements)):
                for permutation in all_permutations(elements[0:i] + elements[i + 1:]):
                    permutation.insert(0, elements[i])
                    yield permutation

    return list(all_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[n - 1]


def problem_25(n):
    """ Return the index of the first Fibonacci number to contain n digits. """
    current = previous = 1
    index = 2

    # int(math.log10(current) is a much faster way of finding the number of digits than len(str(current))
    while int(math.log10(current)) + 1 < n:
        current += previous
        previous = current - previous
        index += 1

    return index


def problem_26(n):
    """ Return the number < n for which 1 / n has the longest recurring cycle in its decimal fraction part.
        For example 1 / 6 = 0.1(6) has a 1-digit recurring cycle. """
    current = 2
    max_cycle = max_int = 0

    while current < n:
        # The first remainder will always be 1
        remainders = [1, 10 % current]

        while remainders[-1] != 0 and remainders[-1] not in remainders[0:-1]:
            remainders += [(remainders[-1] * 10) % current]

        if remainders[-1] == 0:
            cycle = 0
        else:
            cycle = len(remainders) - 1

        if cycle > max_cycle:
            max_cycle = cycle
            max_int = current

        current += 1

    return max_int


def problem_27():
    """ Return the product of a and b, for the quadratic expression n^2 + an + b producing the maximum
        number of primes for consecutive values of n, starting with n = 0.
        math.abs(a) <= 1000 and math.abs(b) <= 1000.
        Since when n = 0, n^2 + an + b = b, b must be a prime. """

    def is_prime(num):
        """ Return True if num is prime. Use a hardcoded list of primes to reduce run time.
            The list is by no means exhaustive but is complete enough for our purposes. """
        primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                  199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                  317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
                  443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
                  577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                  701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
                  839, 853, 857, 859, 864, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977,
                  983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091,
                  1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217,
                  1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321,
                  1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471,
                  1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583,
                  1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709,
                  1721, 1723]

        return num in primes

    a_max = b_max = n_max = 0
    for a in range(-1000, 1000 + 1):
        for b in range(-1000, 1000 + 1):
            n = 0
            while is_prime(abs(n ** 2 + a * n + b)):
                n += 1

            if n > n_max:
                n_max = n
                a_max = a
                b_max = b

    return a_max * b_max


if __name__ == "__main__":
    start_time = time.time()
    print(problem_27())
    print("--- %s seconds ---" % (time.time() - start_time))
