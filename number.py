# Classe pour déterminer les propriétés de certains nombres

import numpy as np


class number:
    def __init__(self, num):
        self.num = num
        self.factor = []

    def isPrime(self):
        mid = round(np.sqrt(self.num))

        if self.num == 0 or self.num == 1:
            print('0 or 1 is an exception.')
            return True
        for x in range(1, int(mid) + 1, 1):
            rest = self.num % x
            if rest == 0:
                self.factor.append(x)
                self.factor.append(self.num / x)

        if len(self.factor) == 2:
            return True
        else:
            return False

    def findFactors(self):
        self.isPrime()
        return sorted(set(self.factor))


a = number(67)

print(a.isPrime())
print(a.findFactors())
