# 1000-digit Fibonacci number
# Problem 25

# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import math
from decimal import Decimal, localcontext



def fiboNum(n):
    with localcontext() as ctx:
        ctx.prec = 2  # 100 digits precision
    p1 = Decimal((1+math.sqrt(5))/2)
    p2 = Decimal((1-math.sqrt(5))/2)
    return Decimal((p1**n - p2**n)/math.sqrt(5))


fiboLen = 0
n = 1
num = 0
while fiboLen < 3:
    n += 1
    num = fiboNum(n)
    fiboLen = len(str(num))

print(num)
print(n)
print(Decimal(math.pi))
