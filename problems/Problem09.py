# Special Pythagorean triplet
# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


import numpy as np
import time

t = time.time()

for a in range(1, 1000, 1):
    for b in range(1, 1000, 1):
        c = np.sqrt(a**2 + b**2)
        if a+b+c == 1000:
            print(a*b*c)
            print(a, b, c)


print(time.time()-t)
# 31 875 000
