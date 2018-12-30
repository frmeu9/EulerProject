# Names scores
# Problem 22

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this
# value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

import string
import time

t = time.time()
alphaDict = dict(zip(string.ascii_uppercase, range(1, 27)))
fileName = open("p022_names.txt", "r")
fileContent = fileName.readlines()[0]
fileContent = fileContent.replace('"', '')
NameList = fileContent.split(',')
NameList = sorted(NameList)
ScoreList = []

for nameIndex in range(len(NameList)):
    nameScore = 0
    for letterIndex in range(len(NameList[nameIndex])):
        nameScore += alphaDict[NameList[nameIndex][letterIndex]]
    ScoreList.append(nameScore*(nameIndex+1))

print(sum(ScoreList))
print(time.time()-t)
# 871 198 282
