import networkx as nx

# Returns the optimal solution for a DAG
def solve_dag(G, weights):
	# We create a weighted copy of G, with a super-source -10
	# and a super-sink 510
	D = nx.DiGraph()
	for u, v in G.edges_iter():
		D.add_edge(u, v, weight = (weights[u] + weights[v]) / 2.0)
		assert type(u) == int and type(v) == int
	for u in G.nodes_iter():
		D.add_edge(-10, u, weight = weights[u] / 2.0)
		D.add_edge(u, 510, weight = weights[u] / 2.0)

	paths = []
	# Keep removing longest paths until only the super-nodes remain
	while nx.number_of_nodes(D) > 2:
		path = longest_path(D)
		if path == []:
			return paths
		paths += [path[1:-1]]
		D.remove_nodes_from(path[1:-1])
	return paths

# This method is modified from the NetworkX source to take into account weights
def longest_path(G):
    dist = {}  # stores [node, distance] pair
    for node in nx.topological_sort(G):
        # pairs of dist,node for all incoming edges
        pairs = [(dist[v][0] + G[v][node]['weight'], v) for v in G.pred[node]]
        if pairs:
            dist[node] = max(pairs)
        else:
            dist[node] = (0, node)
    node, (length, _) = max(dist.items(), key=lambda x: x[1])
    path = []
    while length > 0:
        path.append(node)
        length, node = dist[node]
    return list(reversed(path))


	# # The completely disconnected case
	# if nx.number_weakly_connected_components(G) == nx.number_of_nodes(G):
	# 	print(file, "RAN FOR:", time.time() - start, "SECONDS, SAW 1 SOLUTIONS.")
	# 	print("SEEN", num_perfect, "PERFECTS.")
	# 	print("COMPLETELY DISCONNECTED")
	# 	print("SCORE:", sum(weights))
	# 	return sum(weights), [[i] for i in range(size)]
	# # The DAG case
	# if nx.is_directed_acyclic_graph(G):
	# 	num_perfect += 1
	# 	current_sol = dag_sol.solve_dag(G, weights)
	# 	current_sol = totalValue(current_sol, weights), current_sol
	# 	print(file, "RAN FOR:", time.time() - start, "SECONDS, SAW 1 SOLUTIONS.")
	# 	print("SEEN", num_perfect, "PERFECTS.")
	# 	print("DAG.")
	# 	print("SCORE:", current_sol[0])
	# 	return current_sol