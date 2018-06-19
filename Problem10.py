# Summation of primes
# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from isprime import isprime

nb = 1
summ = 0
limite = 2000000

# while nb < 2000000:
#     factor = []
#     nb += 1
#     mid = np.sqrt(nb)
#     mid = round(mid)
#
#     if nb % 2 == 0 and nb != 2:
#         continue
#
#     for x in range(1, int(mid) + 1, 1):
#         rest = nb % x
#         if rest == 0:
#             factor.append(x)
#             factor.append(nb / x)
#
#     if len(factor) == 2:
#         summ += nb

while nb < limite:
    nb += 1
    if isprime(nb) is True:
        summ += nb
    else:
        continue


print(summ)
# 142913828922
# takes too much time
