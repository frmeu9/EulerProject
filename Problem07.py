# 10001st prime
# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import time
from number import number

t = time.time()
listOfPrime = []

nb = 1
limite = 10001


# while len(listOfPrime) < 10001:
#     factor = []
#     nb += 1
#     mid = np.sqrt(nb)
#     mid = round(mid)
#
#     if nb % 2 == 0 and nb != 2:
#         continue
#
#     for x in range(1, int(mid)+1, 1):
#         rest = nb % x
#         if rest == 0:
#             factor.append(x)
#             factor.append(nb/x)
#
#     if len(factor) == 2:
#         listOfPrime.append(nb)

while len(listOfPrime) < limite:
    nb += 1
    a = number(nb)
    if a.isPrime() is True:
        listOfPrime.append(nb)


print(max(listOfPrime))
print(time.time()-t)

# 104 743
