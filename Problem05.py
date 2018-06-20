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
# checklist_opt = [11, 12, 13, 14, 15, 16, 17, 18, 19]
# print(checklist)


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
# 232792560
