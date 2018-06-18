# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import numpy as np

nb = np.linspace(1, 1000, num=1000)
# index 0 is first element of the list
# index 999 is the last
sum_nb = 0

for i in range(999):
    if np.mod(nb[i], 3) == 0 or np.mod(nb[i], 5) == 0:
        sum_nb = sum_nb + nb[i]

print(sum_nb)
