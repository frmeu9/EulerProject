# Function to determine if a number is a prime number or not

import numpy as np


def isprime(nb):
    factor = []
    mid = np.sqrt(nb)
    mid = round(mid)

    if nb == 0 or nb == 1:
        print('0 or 1 is an exception.')
        return True
    for x in range(1, int(mid) + 1, 1):
        rest = nb % x
        if rest == 0:
            factor.append(x)
            factor.append(nb / x)

    if len(factor) == 2:
        # print("True")
        return True
    else:
        # print("False")
        return False
