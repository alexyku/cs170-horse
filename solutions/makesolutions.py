import networkx as nx
import numpy as np
import random
import time
import glob
import os.path
import sys

num_perfect = 0

# Utility functions:
# Finds the value of a single path
value = lambda path, weights: len(path) * sum([weights[i] for i in path])
# Finds the value of the entire solution
totalValue = lambda sol, weights: sum([value(p, weights) for p in sol])
# Finds what the value of a Rudrata cycle would be
bestPossibleSimple = lambda weights: sum(weights) * len(weights)
# Finds what the value of a Rudrata cycles in each weakly connected component
def bestPossible(components, weights):
	out = 0
	size = 0
	for component in components:
		out += sum([weights[i] for i in component])*len(component)
	return out
# Finds the length of the longest path in a solution
maxPath = lambda sol: max([len(p) for p in sol])



# Generates one randomized solution for G
def solve_graph(G, size, weights):
	# We start with each vertex in a different path and arrange our paths
	# in random order.
	paths = [[i] for i in range(size)]
	random.shuffle(paths)
	# Then for each path p in our list...
	paths = build_paths(G, paths, weights)
	paths = improve_paths(G, paths, weights)
	return totalValue(paths, weights), paths



# Builds some pretty good paths
def build_paths(G, paths, weights):
	i = 0
	while i < len(paths):
		while True:
			# ...check if the last element in p...
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
	return paths



# Improves a given set of paths, by inserting them into each other if possible
def improve_paths(G, paths, weights):
	i = 0
	# For each path
	while i < len(paths):
		p = 0
		# For each element in that path
		current_path = paths[i]
		while p < len(current_path) - 1:
			if not i < len(paths):
				break
			# For each other path
			for j in range(len(paths)):
				if not p < len(current_path) - 1:
					continue
				# Pick an adjacent pair of elements in the current path
				current_path = paths[i]
				parent = current_path[p]
				child = current_path[p + 1]
				# And consider the other paths
				other_path = paths[j]
				other_child = other_path[0]
				other_parent = other_path[-1]
				if i == j:
					continue
				# Combine the paths if possible
				if other_child in G.neighbors(parent) and child in G.neighbors(other_parent):
					paths[i] = current_path[:p+1] + other_path + current_path[p+1:]
					if j < i:
						i -= 1
					paths.pop(j)
					break
			p += 1
		i += 1
	return paths



# Works on solution for time
def solve(file, timeout = 5):
	# Wow much global such program
	global num_perfect

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
	G = nx.DiGraph()
	weights = [0] * size
	for i in range(size):
		neighbors = matrix[i]
		weight = neighbors[i]
		weights[i] = weight
		G.add_node(i)
		G.add_edges_from([(i, j) for j in range(size) if neighbors[j] and j != i])
	# Run solve_graph until we're out of time!
	num_seen = 1
	num_seen_since_improvement = 1
	components = nx.weakly_connected_components(G)
	# print([i for i in components])
	stop_at = bestPossible(components, weights)
	current_sol = solve_graph(G, size, weights)
	while time.time() - start < timeout:
		if current_sol[0] == stop_at:
			#  or num_seen_since_improvement > max_seen_since_improvement
			num_perfect += 1
			# If we find a Rudrata path we're done
			break
		num_seen += 1
		num_seen_since_improvement += 1
		next_sol = solve_graph(G, size, weights)
		if next_sol[0] > current_sol[0]:
			current_sol = next_sol
			num_seen_since_improvement = 0
	# Useful information is printed
	print(file, "RAN FOR:", time.time() - start, "SECONDS, SAW", num_seen, "SOLUTIONS.")
	print("SEEN", num_perfect, "PERFECTS.")
	print("SCORE:", current_sol[0])
	return current_sol
		


# Given that test cases are in path, generate solutions and
# the scores to those solutions
def make_solutions(path, sol_path, score_path, timeout = 5):
	files = glob.glob(path + "/*.in")
	shorter = min([len(f) for f in files])

	# Since there are no leading 0's
	files = ( sorted([f for f in files if len(f) == shorter])
			+ sorted([f for f in files if len(f) == shorter + 1])
			+ sorted([f for f in files if len(f) == shorter + 2]))
	# print(files)

	with open(sol_path, "w") as solution_file, open(score_path, "w") as score_file: 
		for file in files:
			score, sol = solve(file, timeout)
			# asfjklegnkqs
			sol = "; ".join([" ".join([str(i) for i in p]) for p in sol])
			solution_file.write(str(sol)+"\n")
			score_file.write(str(score)+"\n")





# Simp: simple best possible value
# Comp: other best possible value
# No: No improve_paths
assert len(sys.argv) > 2
input_path = sys.argv[1]
output_path = sys.argv[2]
if len(sys.argv) > 3:
	timeout = int(sys.argv[3])

if os.path.isfile(output_path + ".out"):
	print(output_path + ".out already exists")
	sys.exit()


make_solutions(input_path, output_path + ".out", output_path + "Scores.txt", timeout)
# make_solutions("../cs170_final_inputs", 'scores.txt')
# (solve("../cs170_final_inputs/3.in"))

