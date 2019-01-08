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


if __name__ == "__main__":
    start_time = time.time()
    print(problem_22("p022_names.txt"))
    print("--- %s seconds ---" % (time.time() - start_time))
