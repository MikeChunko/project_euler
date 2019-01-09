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


if __name__ == "__main__":
    start_time = time.time()
    print(problem_25(1000))
    print("--- %s seconds ---" % (time.time() - start_time))
