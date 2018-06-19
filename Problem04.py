# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


palin = []

for i in range(100, 1000, 1):
    for j in range(100, 1000, 1):
        rep = i*j
        rep = str(rep)
        if rep == rep[::-1]:
            palin.append(i*j)


print(max(palin))
