# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million
# find the sum of the even-valued terms.

import numpy as np
import time

t = time.time()
# Générer la suite de Fibonacci

fibo = [1, 2]
last = len(fibo)-1
sum_fibo = 0

while fibo[last] < 4000000:
    new = fibo[last] + fibo[last-1]
    fibo.append(new)
    last = len(fibo) - 1


# Trouver la somme des nombres pairs
for i in range(len(fibo)):
    if np.mod(fibo[i], 2) == 0:
        sum_fibo += fibo[i]

print(sum_fibo)
print(time.time()-t)
