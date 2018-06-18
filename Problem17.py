# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

import numpy as np

numList = np.linspace(1, 1000, num=1000)
numList_str = []

for num in range(len(numList)):
    numList_str.append(str(numList[num]))
    numList_str[num] = numList_str[num].rstrip('.0')

numList_str[999] = '1000'