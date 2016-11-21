from random import random

out = open("test1.in", "w")

grid = [[0] * 500 for _ in range(500)]

for i in range(500):
	# try:
	# 	grid[i][i - 5] = 1
	# except:
	# 	1
	try:
		grid[i][i + 5] = 1
	except:
		1
	if i % 10 < 4:
		# try:
		# 	grid[i][i - 4] = 1
		# except:
		# 	1
		try:
			grid[i][i + 6] = 1
		except:
			1
	if i % 10 > 5:
		# try:
		# 	grid[i][i - 6] = 1
		# except:
		# 	1
		try:
			grid[i][i + 4] = 1
		except:
			1

	grid[i][i] = int(10 * random())

for k in range(80):
	i = int(500*random())
	grid[i][i] = 99

out.write("500")
out.write("\n")
for i in range(500):
	for j in range(500):
		grid[i][j] = str(grid[i][j])
	out.write(" ".join(grid[i]))
	out.write("\n")

