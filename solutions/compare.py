import numpy as np
import sys

assert len(sys.argv) == 3, sys.argv

twenty = []

with open(sys.argv[1] + 'Scores.txt', "r") as file:
	for line in file:
		twenty += [line]

five = []

with open(sys.argv[2] + 'Scores.txt', "r") as file:
	for line in file:
		five += [line]
		# if line[0] == "S":
		# 	their_scores += [line.strip().split(" ")[-1]]


twenty = np.array(twenty).astype(int)
five = np.array(five).astype(int)

print("First total:", sum(twenty), "Second total:", sum(five))
print( "First is better on", np.count_nonzero(np.greater(twenty, five)))
print( "First is worse on", np.count_nonzero(np.less(twenty, five)))
print([i + 1 for i in range(600) if five[i] > twenty[i]])
# [38, 49, 84, 91, 105, 130, 138, 142, 198, 211, 213, 223, 258, 291, 304, 305, 313, 314, 345, 369, 386, 394, 422, 423, 433, 489, 498, 554, 557, 577]