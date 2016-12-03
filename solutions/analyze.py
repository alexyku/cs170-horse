import glob
import numpy as np
import matplotlib.pyplot as plt

files = glob.glob("solutions/Best*Scores.txt")

scores = []
for file in files:
	print(file)
	score = 0
	with open(file, "r") as f:
		for line in f:
			score += int(line.strip())
	scores += [score]

scores = np.array(scores)
print(scores)
plt.scatter(np.arange(len(scores)), scores)
lims = plt.ylim()
plt.ylim([3.19 * 10 ** 9, lims[1]]) 
plt.show()




