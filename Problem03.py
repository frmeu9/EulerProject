# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import numpy as np


num = 600851475143
factor = []

# Trouver tous les facteurs du nombre
# On test seulement les nombres allant de 0 à la racine de num


def fct(nb, liste):
    middle = np.sqrt(nb)
    middle = np.round(middle)
#   print(middle)

    for x in range(1, int(middle), 1):
        rest = nb % x
        if rest == 0:
            liste.append(x)
            liste.append(nb/x)
    liste.sort()
#   print(list)


fct(num, factor)


# Trouver les nombres premiers et trouver le plus grand
prime = []

for i in range(len(factor)-1):
    factor2 = []
    fct(factor[i], factor2)
    if len(factor2) == 2:
        prime.append(factor[i])


print(max(prime))
