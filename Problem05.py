# Smallest multiple
# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Il faut sortir tous les multiples de tous les nombres de 1 à 20 et trouver le premier multiple commun
# Il faut trouver le LCM (least common multiple)


import numpy as np
import time

t = time.time()

checklist = np.linspace(1, 20, num=20)
num = 0
comm = 0


while comm == 0:
    num += 20
    rest = []
    for i in range(1, len(checklist), 1):
        rest.append(num % i)
        if max(rest) > 0:
            break
    if max(rest) == 0:
        comm = 1


print(num)
print(time.time()-t)
# 232 792 560

# 20 = 2^2 * 5
# 19 = 19
# 18 = 2 * 3^2
# 17 = 17
# 16 = 2^4
# 15 = 3 * 5
# 14 = 2 * 7
# 13 = 13
# 11 = 11
# ANSWER: 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232 792 560
