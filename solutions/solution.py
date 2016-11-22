import networkx as nx
import numpy as np
import random
import time

TIME_OUT_SECONDS = 30


value = lambda path, weights: len(path) * sum([weights[i] for i in path])

totalValue = lambda sol, weights: sum([value(p, weights) for p in sol])

bestPossible = lambda weights: sum(weights) * len(weights)

maxPath = lambda sol: max([len(p) for p in sol])

def solve_graph(G, size, weights):
	# We start with each vertex in a different path...
	paths = [[i] for i in range(size)]
	# ...and arrange our paths in random order.
	random.shuffle(paths)

	# Then for each path $p$ in our list...
	i = 0
	while i < len(paths):
		while True:
			# ...check if the last element in $p$...
			end = paths[i][-1]

			next = -1
			nextVal = -1

			for j in range(len(paths)):

				if j == i:
					continue

				# ...matches the first element in any other path, and if so,
				# choose the longest such path.

				start = paths[j][0]
				if start in G.neighbors(end) and value(paths[j], weights) > nextVal:
					next = j
					nextVal = value(paths[j], weights)

			# If not, go on to the next path...
			if nextVal == -1:
				break

			# ...but if so, append the two paths, and delete one of them.
			paths[i] = paths[i] + paths[next]
			paths.pop(next)
			if next < i:
				i -= 1

		i += 1

	# We return both the value of the solution, and a list of paths
	return totalValue(paths, weights), paths




def solve(file):
	# Start the timer!
	start = time.time()

	# Build the adjacency matrix!
	matrix = []
	size = 0
	with open(file, "r") as f:
		size = int(f.readline().strip())
		for i in range(size):
			matrix.append([int(s) for s in f.readline().strip().split(" ")])

	# Build the nx Graph!
	G = nx.Graph()
	weights = [0] * size
	for i in range(size):
		neighbors = matrix[i]
		weight = neighbors[i]
		weights[i] = weight
		G.add_node(i)
		G.add_edges_from([(i, j) for j in range(size) if neighbors[j]])
		# G.add_weighted_edges_from([(i, j, weight / 2.0) for j in range(size) if neighbors[j]])

	# Run solve_graph until we're out of time!
	num_seen = 1
	stop_at = bestPossible(weights)
	current_sol = solve_graph(G, size, weights)
	while time.time() - start < TIME_OUT_SECONDS:
		if current_sol[0] == stop_at:
			break
		num_seen += 1
		next_sol = solve_graph(G, size, weights)
		if next_sol[0] > current_sol[0]:
			current_sol = next_sol



	print("RAN FOR:", time.time() - start, "SECONDS, SAW", num_seen, "SOLUTIONS")
	# print(current_sol)
	# print (maxPath(current_sol[1]), totalValue(current_sol[1], weights))
	return current_sol[0]
		
print(solve("1.in"))
print(solve("2.in"))
print(solve("3.in"))
print(solve("../sample1.in"))
print(solve("../sample2.in"))
print(solve("../sample3.in"))
print(solve("02_01_00.in"))
print(solve("0046.in"))
print(solve("0037.in"))
data = [solve("3.in")[1] for _ in range(10)]
print(data, max(data))


