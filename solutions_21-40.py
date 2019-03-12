# File name: solutions_21-40.py
# Author: Michael Chunko
# Date created: 1/5/19
# Python Version: 3.7

# This file contains the algorithms used for solving problems 21 through 40 (inclusive) from projecteuler.net

import math
import time
import helpers


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
                break
            if j - i in abundant_numbers:
                break

    return sums


def problem_24(n):
    """ Return the nth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        A lexicographic permutation is one where the list of all permutations is sorted numerically/alphabetically"""

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
    primes = helpers.eratosthenes_sieve(10000)

    def is_prime(num):
        """ Return True if num is prime. Use a hardcoded list of primes to reduce run time.
            The list is by no means exhaustive but is complete enough for our purposes. """
        return num in primes

    a_max = b_max = n_max = 0
    b_range = helpers.eratosthenes_sieve(1000)
    for i in range(len(b_range)):
        b_range[i] = -b_range[i]

    b_range += [0] + helpers.eratosthenes_sieve(1000)

    for b in b_range:
        for a in range(-1000, 1000 + 1):
            n = 0
            while is_prime(abs(n ** 2 + a * n + b)):
                n += 1

            if n > n_max:
                n_max = n
                a_max = a
                b_max = b

    return a_max * b_max


def problem_28(n):
    """ Return the sum of the numbers on the diagonals of a n*n spiral.
        The spiral is made by starting with '1' at the center and moving to the right in a clockwise direction.
        A 3*3 would be: 7 8 9
                        6 1 2
                        5 4 3.
        Input n: Must be an odd number. """

    # Initialize the grid making sure it's a deep copy of '0's
    grid = []
    for i in range(0, n):
        tmp = []
        for j in range(0, n):
            tmp += [0]
        grid += [tmp]

    # Create the spiral
    current = iteration = 1
    i = j = n // 2
    grid[i][j] = current
    current += 1
    while j < n and i < n:

        for k in range(0, iteration):
            j += 1
            if j >= n or i >= n:
                break
            grid[i][j] = current
            current += 1

        if j >= n or i >= n:
            break

        for k in range(0, iteration):
            i += 1
            if j >= n or i >= n:
                break
            grid[i][j] = current
            current += 1

        iteration += 1

        for k in range(0, iteration):
            j -= 1
            if j >= n or i >= n:
                break
            grid[i][j] = current
            current += 1

        for k in range(0, iteration):
            i -= 1
            if j >= n or i >= n:
                break
            grid[i][j] = current
            current += 1

        iteration += 1

    # Calculate the sum of the diagonals
    running_sum = 0

    i = j = 0
    while j < n and i < n:
        running_sum += grid[i][j]
        i += 1
        j += 1

    i = 0
    j = n - 1
    while j >= 0 and i < n:
        running_sum += grid[i][j]
        i += 1
        j -= 1

    # Remove the double-counted center number
    running_sum -= 1

    return running_sum


def problem_29(n):
    """ Return the number of distinct terms in the sequence generate by a^b for 2 <= a <= n and 2 <= b <= n.
        If the upper limit on a and b were 4, then the sequence would be: 4, 8, 9, 16, 27, 64, 81, 256. """
    sequence = set()
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            sequence.add(math.pow(a, b))

    return len(sequence)


def problem_30(n):
    """ Return the sum of all the numbers that can be written as the sum of nth powers of their digits. """
    result = 0

    for i in range(2, 354294 + 1):  # 354294 is a reasonable upper bound
        temp = i
        summation = 0
        while temp / 10 != 0:
            summation += math.pow(temp % 10, n)
            temp //= 10

        if summation == i:
            result += i

    return result


def problem_31(n, coins):
    """ Return the number of ways n can be made by using any number of coins.
        Input n: The value to be made in pence
        Input coins: A list of all possible coins.
        The inputs must be whole numbers due to problems representing decimal numbers in binary. """
    if not coins or n < 0:
        return 0
    if n == 0:
        return 1

    return problem_31(n - coins[0], coins) + problem_31(n, coins[1:])


def problem_32(n):
    """ Find the sum of all products whose multiplicand/multiplier/product identity can be written as 1-n pandigital.
        An n-digit number is pandigital if each digits 1-n appears exactly once"""

    def problem_32_helper(digits):
        if len(digits) != n:
            return False
        for i in range(1, n + 1):
            if str(i) not in digits:
                return False
        return True

    pandigitals = []

    for a in range(1, 10 ** (n - 3)):
        for b in range(a, 10 ** (n - 3)):
            if len(str(a) + str(b) + str(a * b)) > 9:
                break
            if problem_32_helper(str(a) + str(b) + str(a * b)) and (a * b) not in pandigitals:
                pandigitals.append(a * b)
                print(pandigitals)

    return sum(pandigitals)


def problem_33():
    """ Return the product of four "curious fractions" when represented
        in its lowest common terms.
        A "curious fraction" is one where the correct simplification can be incorrectly obtained by
        cancelling out a digit in the numerator and denominator.
        For our purposes, we're only counting "curious fractions" less than one in value, and with two digits
        in the numerator and denominator.
        The fractions must also be non-trivial, meaning the shared digit cannot be a zero. """

    def shared_digit(a, b):
        """ Return the digits that is shared between the two numbers.
            Return -1 if no digit is shared.
            For example, shared_digits(49, 98) would return (9, 90). """
        str_a, str_b = str(a), str(b)
        for i in range(0, 2):
            if str_a[i] in str_b:
                return int(str_a[1 - i]), int(str_b[1 - str_b.index(str_a[i])])
        return -1

    fractions = []

    for numerator in range(10, 99 + 1):
        # There are known to be only four of these fractions
        if len(fractions) == 4:
            break
        for denominator in range(numerator + 1, 99 + 1):
            if shared_digit(numerator, denominator) != -1:
                a, b = shared_digit(numerator, denominator)
                if numerator / 10 != a and denominator / 10 != b and a != 0 and b != 0:
                    if a / b == numerator / denominator:
                        fractions.append([numerator, denominator])
                        print(numerator, denominator, a, b)

    product = 1
    for x in fractions:
        product *= x[0] / x[1]

    return product


def problem_34():
    """ Return the sum of all numbers which are equal to the sum of the factorial of their digits. """
    factorials = []
    for i in range(0, 10):
        factorials.append(math.factorial(i))

    running_total = 0

    for i in range(10, 2540161):
        total = 0
        for x in str(i):
            total += factorials[int(x)]

        if i == total:
            running_total += i

    return running_total


def problem_35(n):
    """ Return the number of circular primes below n.
        A number is a circular prime if it and all of its circular rotations are prime. """
    result = [2, 3, 5]
    primes = helpers.eratosthenes_sieve(n)

    for i in range(7, n + 1, 2):
        if i % 5 != 0 and i % 3 != 0 and i not in result:
            for j in helpers.number_rotations(i):
                if j not in primes:
                    break
            else:
                result.append(helpers.number_rotations(i))
                print(i)

    return len(result)


if __name__ == "__main__":
    start_time = time.time()
    print(problem_35(10 ** 5))
    print("--- %s seconds ---" % (time.time() - start_time))
