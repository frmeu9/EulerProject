# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from number import number
import time

t = time.time()
num = 600851475143

# Trouver tous les facteurs du nombre
# On teste seulement les nombres allant de 0 à la racine de num

a = number(num)
factor = a.findFactors()

# Trouver les nombres premiers et trouver le plus grand
primeList = []

for i in range(len(factor)-1):
    a = number(factor[i])
    if a.isPrime() is True:
        primeList.append(factor[i])


print(max(primeList))
print(time.time()-t)
# 6 857
