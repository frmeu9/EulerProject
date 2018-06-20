# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from isprime import isprime
from FindFactors import FindFactors
import time

t = time.time()
num = 600851475143
factor = []

# Trouver tous les facteurs du nombre
# On test seulement les nombres allant de 0 à la racine de num

factor = FindFactors(num)

# Trouver les nombres premiers et trouver le plus grand
prime = []

for i in range(len(factor)-1):
    if isprime(factor[i]) is True:
        prime.append(factor[i])


print(max(prime))
print(time.time()-t)
# 6857
