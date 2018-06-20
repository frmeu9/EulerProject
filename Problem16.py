# Power digit sum
# Problem 16

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

import time

t = time.time()
num = 2**1000
num_str = str(num)
length = len(num_str)
somme = 0
for i in range(length):
    somme += int(num_str[i])

print(somme)
print(time.time()-t)
# 1366
