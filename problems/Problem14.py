# Longest Collatz sequence
# Problem 14

# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time

t = time.time()
listchain = []

for start in range(1, 1000000):
    currentNum = start
    tempList = []
    tempList.append(currentNum)
    while currentNum != 1:
        if currentNum % 2 == 0:
            currentNum = currentNum/2
            tempList.append(currentNum)
        else:
            currentNum = 3*currentNum + 1
            tempList.append(currentNum)
    listchain.append(tempList)

length = []

for i in range(len(listchain)):
    length.append(len(listchain[i]))

idx = length.index(max(length))
# print(idx)
print(listchain[idx][0])
print(time.time()-t)
# 837 799
