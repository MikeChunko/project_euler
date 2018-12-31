# File name: solutions.py
# Author: Michael Chunko
# Date created: 12/23/18
# Python Version: 3.7

import math
import time
import sys


# Problems 1-7 were completed separately and are not current included in this file.
# They may be resolved and added at a later date

def problem_8(n):
    """ Return the product of the n adjacent digits in the provided number with the greatest product.
        Previous product represents the sum of n - 1 adjacent digits so that when the next product is found,
        rather than multiplying n numbers again, previous product can instead be multiplied by a single number. """
    big_num = "731671765313306249192251196744265747423553491949349698352031277450632623957831801698480\n" \
              "186947885184385861560789112949495459501737958331952853208805511125406987471585238630507\n" \
              "156932909632952274430435576689664895044524452316173185640309871112172238311362229893423\n" \
              "380308135336276614282806444486645238749303589072962904915604407723907138105158593079608\n" \
              "667017242712188399879790879227492190169972088809377665727333001053367881220235421809751\n" \
              "254540594752243525849077116705560136048395864467063244157221553975369781797784617406495\n" \
              "514929086256932197846862248283972241375657056057490261407972968652414535100474821663704\n" \
              "844031998900088952434506585412275886668811642717147992444292823086346567481391912316282\n" \
              "458617866458359124566529476545682848912883142607690042242190226710556263211111093705442\n" \
              "175069416589604080719840385096245544436298123098787992724428490918884580156166097919133\n" \
              "875499200524063689912560717606058861164671094050775410022569831552000559357297257163626\n" \
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
        Return "-1" if no valid pythagorean triple is found.
        Use a combination of loops to reasonably efficiently find pythagorean triples then check if they match
        the conditions. """
    for a in range(1, n):
        b = a + 1
        c = b + 1
        while c < n:
            while c ** 2 < a ** 2 + b ** 2:
                c += 1
            if c ** 2 == a ** 2 + b ** 2 and a + b + c == n:
                return a * b * c
            b += 1

    return -1


def problem_10(n):
    """ Return the sum of all primes below n.
        Use a very simple prime finder. """
    primes = [2, 3, 5]

    # Basic prime finder
    # Not super efficient but it works
    for n in range(7, n, 2):
        if n % 5 != 0:
            is_prime = True
            for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    is_prime = False
                    break

            if is_prime:
                primes += [n]
    print(primes)
    return sum(primes)


# Currently incredibly slow but yields the correct answer
def problem_12(n):
    """ Return the value of the first triangle number to have over n divisors.
        Return "-1" if none are found.
        Manually check to see which numbers are divisors and keep a running tally to see if the value crosses n. """
    current_triangle_num = 1

    for i in range(2, sys.maxsize):
        # 1 and the number itself will always be divisors
        divisor_count = 2
        current_triangle_num += i
        print(current_triangle_num)

        for j in range(2, current_triangle_num // 2 + 1):
            if current_triangle_num % j == 0:
                divisor_count += 1
                if divisor_count > n:
                    return current_triangle_num
    return -1


def problem_13(n):
    """ Return the first n digits of the sum of the 100 following 50-digit numbers.
        Use simple list comprehension and the built-in sum() function. """
    numbers_as_str = "37107287533902102798797998220837590246510135740250\n" \
                     "46376937677490009712648124896970078050417018260538\n" \
                     "74324986199524741059474233309513058123726617309629\n" \
                     "91942213363574161572522430563301811072406154908250\n" \
                     "23067588207539346171171980310421047513778063246676\n" \
                     "89261670696623633820136378418383684178734361726757\n" \
                     "28112879812849979408065481931592621691275889832738\n" \
                     "44274228917432520321923589422876796487670272189318\n" \
                     "47451445736001306439091167216856844588711603153276\n" \
                     "70386486105843025439939619828917593665686757934951\n" \
                     "62176457141856560629502157223196586755079324193331\n" \
                     "64906352462741904929101432445813822663347944758178\n" \
                     "92575867718337217661963751590579239728245598838407\n" \
                     "58203565325359399008402633568948830189458628227828\n" \
                     "80181199384826282014278194139940567587151170094390\n" \
                     "35398664372827112653829987240784473053190104293586\n" \
                     "86515506006295864861532075273371959191420517255829\n" \
                     "71693888707715466499115593487603532921714970056938\n" \
                     "54370070576826684624621495650076471787294438377604\n" \
                     "53282654108756828443191190634694037855217779295145\n" \
                     "36123272525000296071075082563815656710885258350721\n" \
                     "45876576172410976447339110607218265236877223636045\n" \
                     "17423706905851860660448207621209813287860733969412\n" \
                     "81142660418086830619328460811191061556940512689692\n" \
                     "51934325451728388641918047049293215058642563049483\n" \
                     "62467221648435076201727918039944693004732956340691\n" \
                     "15732444386908125794514089057706229429197107928209\n" \
                     "55037687525678773091862540744969844508330393682126\n" \
                     "18336384825330154686196124348767681297534375946515\n" \
                     "80386287592878490201521685554828717201219257766954\n" \
                     "78182833757993103614740356856449095527097864797581\n" \
                     "16726320100436897842553539920931837441497806860984\n" \
                     "48403098129077791799088218795327364475675590848030\n" \
                     "87086987551392711854517078544161852424320693150332\n" \
                     "59959406895756536782107074926966537676326235447210\n" \
                     "69793950679652694742597709739166693763042633987085\n" \
                     "41052684708299085211399427365734116182760315001271\n" \
                     "65378607361501080857009149939512557028198746004375\n" \
                     "35829035317434717326932123578154982629742552737307\n" \
                     "94953759765105305946966067683156574377167401875275\n" \
                     "88902802571733229619176668713819931811048770190271\n" \
                     "25267680276078003013678680992525463401061632866526\n" \
                     "36270218540497705585629946580636237993140746255962\n" \
                     "24074486908231174977792365466257246923322810917141\n" \
                     "91430288197103288597806669760892938638285025333403\n" \
                     "34413065578016127815921815005561868836468420090470\n" \
                     "23053081172816430487623791969842487255036638784583\n" \
                     "11487696932154902810424020138335124462181441773470\n" \
                     "63783299490636259666498587618221225225512486764533\n" \
                     "67720186971698544312419572409913959008952310058822\n" \
                     "95548255300263520781532296796249481641953868218774\n" \
                     "76085327132285723110424803456124867697064507995236\n" \
                     "37774242535411291684276865538926205024910326572967\n" \
                     "23701913275725675285653248258265463092207058596522\n" \
                     "29798860272258331913126375147341994889534765745501\n" \
                     "18495701454879288984856827726077713721403798879715\n" \
                     "38298203783031473527721580348144513491373226651381\n" \
                     "34829543829199918180278916522431027392251122869539\n" \
                     "40957953066405232632538044100059654939159879593635\n" \
                     "29746152185502371307642255121183693803580388584903\n" \
                     "41698116222072977186158236678424689157993532961922\n" \
                     "62467957194401269043877107275048102390895523597457\n" \
                     "23189706772547915061505504953922979530901129967519\n" \
                     "86188088225875314529584099251203829009407770775672\n" \
                     "11306739708304724483816533873502340845647058077308\n" \
                     "82959174767140363198008187129011875491310547126581\n" \
                     "97623331044818386269515456334926366572897563400500\n" \
                     "42846280183517070527831839425882145521227251250327\n" \
                     "55121603546981200581762165212827652751691296897789\n" \
                     "32238195734329339946437501907836945765883352399886\n" \
                     "75506164965184775180738168837861091527357929701337\n" \
                     "62177842752192623401942399639168044983993173312731\n" \
                     "32924185707147349566916674687634660915035914677504\n" \
                     "99518671430235219628894890102423325116913619626622\n" \
                     "73267460800591547471830798392868535206946944540724\n" \
                     "76841822524674417161514036427982273348055556214818\n" \
                     "97142617910342598647204516893989422179826088076852\n" \
                     "87783646182799346313767754307809363333018982642090\n" \
                     "10848802521674670883215120185883543223812876952786\n" \
                     "71329612474782464538636993009049310363619763878039\n" \
                     "62184073572399794223406235393808339651327408011116\n" \
                     "66627891981488087797941876876144230030984490851411\n" \
                     "60661826293682836764744779239180335110989069790714\n" \
                     "85786944089552990653640447425576083659976645795096\n" \
                     "66024396409905389607120198219976047599490197230297\n" \
                     "64913982680032973156037120041377903785566085089252\n" \
                     "16730939319872750275468906903707539413042652315011\n" \
                     "94809377245048795150954100921645863754710598436791\n" \
                     "78639167021187492431995700641917969777599028300699\n" \
                     "15368713711936614952811305876380278410754449733078\n" \
                     "40789923115535562561142322423255033685442488917353\n" \
                     "44889911501440648020369068063960672322193204149535\n" \
                     "41503128880339536053299340368006977710650566631954\n" \
                     "81234880673210146739058568557934581403627822703280\n" \
                     "82616570773948327592232845941706525094512325230608\n" \
                     "22918802058777319719839450180888072429661980811197\n" \
                     "77158542502016545090413245809786882778948721859617\n" \
                     "72107838435069186155435662884062257473692284509516\n" \
                     "20849603980134001723930671666823555245252804609722\n" \
                     "53503534226472524250874054075591789781264330331690"
    numbers_as_int = [int(i) for i in numbers_as_str.split("\n")]
    summation = sum(numbers_as_int)
    return str(summation)[:n]


def problem_14(n):
    """ Given the iterative sequence defined as: n → n/2 (n is even), n → 3n + 1 (n is odd)
        Return the starting number, under n, which produces the longest chain before reaching 1.
        Use the fact that any power of 2 has a known distance to the end to speed up run time. """
    longest = (0, 1)  # (chain length, number)
    memo = {}

    for i in range(1, n):
        current_chain = 1
        current_number = i

        while current_number != 1:
            if current_number in memo:
                current_chain += memo[current_number]
                break

            # True if current_number is a power of 2
            if not current_number & (current_number - 1):
                while current_number > 1:
                    current_number /= 2
                    current_chain += 1
                break

            if current_number % 2 == 0:
                current_number = current_number // 2
            else:
                current_number = 3 * current_number + 1

            current_chain += 1

        if current_chain > longest[0]:
            longest = (current_chain, i)
        memo[i] = current_chain

    return longest[1]


def problem_15(n):
    """ Return the number of lattice paths for a n x n grid where you always start in the top left corner
        and can only move down and right.
        Through experimentation, it's found that the answer is equal to the center number on the 2*nth row of
        Pascal's triangle. """

    def pascals_triangle(previous_row):
        new_row = []
        for i in range(0, len(previous_row) - 1):
            new_row += [previous_row[i] + previous_row[i + 1]]
        new_row = [1] + new_row + [1]
        return new_row

    current_row = [1, 1]
    iteration = 1
    while iteration < n * 2:
        iteration += 1
        current_row = pascals_triangle(current_row)

    # In this case the index of the center number is always equal to n
    return current_row[n]


def problem_16(n):
    """ Return the sum of the digits of 2 ** n.
        Use list comprehension to solve. """
    return sum([int(x) for x in str(2 ** n)])


def problem_17(n):
    """ Return the sum of the letters used to write the number from 1  to n (inclusive).
        n: an integer between 1 and 1000 (inclusive).
        The code is ugly but simply goes through a series of cases, constructing the length of the word to represent
        various numbers. """

    # Dictionaries containing the lengths of various numbers
    singles_place = [3, 3, 5, 4, 4, 3, 5, 5, 4]  # lengths for [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ten = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]  # lengths for [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    tens_place = [5, 6, 6, 5, 5, 7, 6, 6]  # lengths for [20, 30, 40, 50, 60, 70, 80, 90]
    hundred = 7  # length of 100
    thousand = 8  # length of 1000

    running_total = 0
    for i in range(1, n + 1):
        if i < 10:
            running_total += singles_place[i - 1]
        elif i < 20:
            running_total += ten[i % 10]
        elif i < 100:
            running_total += tens_place[i // 10 - 2]
            if i % 10 != 0:
                running_total += singles_place[i % 10 - 1]
        elif i < 1000:
            running_total += singles_place[i // 100 - 1]
            running_total += hundred + 3  # 3 represents the length of 'and'
            if i % 100 == 0:
                running_total -= 3  # Remove the 'and' if there is nothing following the 'hundred'
            elif i % 100 < 10:
                running_total += singles_place[i % 100 - 1]
            elif i % 100 < 20:
                running_total += ten[i % 100 - 10]
            else:
                running_total += tens_place[(i % 100) // 10 - 2]
                if i % 10 != 0:
                    running_total += singles_place[i % 10 - 1]
        elif i == 1000:
            running_total += singles_place[0] + thousand

    return running_total


if __name__ == "__main__":
    start_time = time.time()
    print(problem_17(1000))
    print("--- %s seconds ---" % (time.time() - start_time))
