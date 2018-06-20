# Sum square difference
# Problem 6

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


import numpy as np
import time


t = time.time()

allNum = np.linspace(1, 100, 100)
SumSq = 0
for i in range(len(allNum)):
    SumSq += allNum[i]**2

sumNum = sum(allNum)
SqAllNum = sumNum**2

print(SqAllNum - SumSq)
print(time.time()-t)
# 25164150
