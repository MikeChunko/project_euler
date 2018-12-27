import math
import time
import sys


def problem_8(n):
    """ Return the product of the n adjacent digits in the provided number with the greatest product. """
    big_num = "731671765313306249192251196744265747423553491949349698352031277450632623957831801698480" \
              "186947885184385861560789112949495459501737958331952853208805511125406987471585238630507" \
              "156932909632952274430435576689664895044524452316173185640309871112172238311362229893423" \
              "380308135336276614282806444486645238749303589072962904915604407723907138105158593079608" \
              "667017242712188399879790879227492190169972088809377665727333001053367881220235421809751" \
              "254540594752243525849077116705560136048395864467063244157221553975369781797784617406495" \
              "514929086256932197846862248283972241375657056057490261407972968652414535100474821663704" \
              "844031998900088952434506585412275886668811642717147992444292823086346567481391912316282" \
              "458617866458359124566529476545682848912883142607690042242190226710556263211111093705442" \
              "175069416589604080719840385096245544436298123098787992724428490918884580156166097919133" \
              "875499200524063689912560717606058861164671094050775410022569831552000559357297257163626" \
              "9561882670428252483600823257530420752963450"

    previous_product = 1
    for i in range(1, n):
        previous_product *= int(big_num[i])

    current_product = previous_product * int(big_num[0])
    maximum = current_product

    for i in range(1, len(big_num) - n):
        current_product = previous_product * int(big_num[i + n - 1])
        if big_num[i] != "0":
            previous_product = current_product / int(big_num[i])
        else:
            previous_product = 1
            for j in range(i + 1, i + n):
                previous_product *= int(big_num[j])

        if current_product > maximum:
            maximum = current_product

    return int(maximum)


def problem_9(n):
    """ Return the product of a, b, and c where a + b + c = n and a, b, and c are a pythagorean triplet.
        Return "-1" if no valid pythagorean triple is found. """
    for a in range(1, n):
        b = a + 1
        c = b + 1
        while c < n:
            while c ** 2 < a ** 2 + b ** 2:
                c += 1
            if c ** 2 == a ** 2 + b ** 2:
                print("Triple found")
                if a + b + c == n:
                    print("Correct found")
                    return a * b * c
            b += 1

    return -1


if __name__ == "__main__":
    start_time = time.time()
    print(problem_9(1000))
    print("--- %s seconds ---" % (time.time() - start_time))
