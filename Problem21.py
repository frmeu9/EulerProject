# Amicable numbers
# Problem 21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). If d(a) = b
# and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

from isprime import isprime
from FindFactors import FindFactors
import time

t = time.time()
am_num = []

for i in range(10000):
    mult = []
    if isprime(i) is True:
        continue
    else:
        mult = FindFactors(i)
        mult.remove(i)
        num2 = sum(mult)
        if isprime(num2) is True:
            continue
        else:
            mult2 = FindFactors(num2)
            mult2.remove(num2)
            sum2 = sum(mult2)
            if sum2 == i and num2 != i:
                am_num.append(i)
                am_num.append(num2)


orderedList = set(am_num)
print(sum(orderedList))
print(time.time()-t)
# 31262
