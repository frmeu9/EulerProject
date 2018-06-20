# Factorial digit sum
# Problem 20

# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

import math
import time

t = time.time()

# num = 100
# prod = 1

# for i in range(1, num+1):
#    prod *= i

prod = math.factorial(100)
prod_str = str(prod)
somme = 0

for j in range(len(prod_str)):
    somme += int(prod_str[j])

print(somme)
print(time.time()-t)
# 648
