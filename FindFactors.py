# Return a list of all factors of a number

import numpy as np


def FindFactors(nb):
    middle = np.sqrt(nb)
    middle = np.round(middle)
    liste = []
    if nb == 1 or nb == 2:
        return

    for x in range(1, int(middle), 1):
        rest = nb % x
        if rest == 0:
            liste.append(x)
            liste.append(nb / x)
    liste.sort()
    return liste
