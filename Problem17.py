# Number letter counts
# Problem 17

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


# Creating list of numbers from 1 to 1000
numList = np.linspace(1, 1000, num=1000)

# Creating list of numbers written in letters from 1 to 1000
numList_str = []

for num in range(len(numList)):
    numList_str.append(str(numList[num]))
    numList_str[num] = numList_str[num].replace('.0', '')


# Creating dictionary
# nb: 'nb_in_letters'

num_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
            60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 1000: 'onethousand'}
# LOOP
numChar = ''
for i in range(len(numList_str)):
    if len(numList_str[i]) == 1 or len(numList_str[i]) == 4:
        numChar += num_dict[int(numList_str[i])]
    if len(numList_str[i]) == 2:
        if numList_str[i][0] == '1':
            numChar += num_dict[int(numList_str[i])]
        elif numList_str[i][0] != '1':
            numChar += num_dict[int(numList_str[i][0])*10]
            if int(numList_str[i][1]) == 0:
                continue
            else:
                numChar += num_dict[int(numList_str[i][1])]
    if len(numList_str[i]) == 3:
        numChar += num_dict[int(numList_str[i][0])] + 'hundred'
        if numList_str[i][1] == '0' and numList_str[i][2] == '0':
            continue
        elif numList_str[i][1] == '1' or numList_str[i][1] == '0':
            numChar += 'and' + num_dict[int(numList_str[i][1:3])]
        elif numList_str[i][1] > '1':
            numChar += 'and' + num_dict[int(numList_str[i][1]) * 10]
            if int(numList_str[i][2]) == 0:
                continue
            else:
                numChar += num_dict[int(numList_str[i][2])]


print(len(numChar))
# 21124
