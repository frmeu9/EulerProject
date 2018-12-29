# Lattice paths
# Problem 15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

import math
import time

t = time.time()
answer = math.factorial(40)/(math.factorial(20)*math.factorial(20))
# Grille de 20x20, il faut faire 20 mouvements à droite et 20 vers le bas
# On compte les permutations des 20 mouvements vers le bas parmis les 40

print(answer)
print(time.time()-t)
# 137 846 528 820
