import numpy as np
from random import random
import io

# max weight of vertices
P = 100
# number of vertices
N = 500

def rbipart(n, pivot=None):
    """returns a random bipartite graph with n vertices as an adjacency matrix"""

    # make adjacency matrix
    adj = np.zeros((n, n), dtype=np.uint8)

    # randomly partition vertices
    if pivot is None:
        pivot = np.random.randint(n)
    a, b = range(pivot), range(pivot, n)
    
    # initialize vertice values
    for i in range(n):
        adj[i][i] = np.random.randint(P)
    
    # randomly connect sets a and b
    for i in a:
        for j in np.random.choice(b, np.random.randint(len(b))):
            adj[i][j] = adj[j][i] = 1 # undirected
    return adj

def pcomplete(n, pct=None):
    """returns a partially complete graph with n vertices"""
    
    # make adjacency matrix
    adj = np.zeros((n, n), dtype=np.uint8)

    # randomly determine percent connectedness
    if pct is None:
        pct = np.random.rand()

    # initialize vertice values
    for i in range(n):
        adj[i][i] = np.random.randint(P)

    # connect approximate percentage of edges
    for i in range(n):
        for j in range(n):
            x = np.random.rand()
            if (x < pct) and (i != j):
                adj[i][j] = 1
    return adj

def caliban(n, param=50):
    """returns the insanity that dwells in Weston's mind"""

    # make adjacency matrix
    adj = np.zeros((n,n), dtype=np.uint8)

    # initialize vertice values
    for i in range(n):
        adj[i][i] = np.random.randint(10) # int(10 * random())

    # connect graph
    for i in range(n):
        try:
            adj[i][i + 5] = 1
        except:
            1
        if i % 10 < 4:
            try:
                adj[i][i + 6] = 1
            except:
                1
        if i % 10 > 5:
            try:
                adj[i][i + 4] = 1
            except:
                1

    # initialize vertice values
    for _ in range(param):
        i = np.random.randint(n) # int(n * random()) 
        adj[i][i] = P - 1

    return adj

def adj_to_str(adj):
    return '\n'.join(' '.join(i.astype('str')) for i in adj)

def print_adj(adj):
    print(adj_to_str(adj))

def write_adj(adj, path):
    with open(path, 'w+') as f:
        f.write(str(N) + '\n')
        f.write(adj_to_str(adj))
        f.close()

# verify if percent conectedness is correct
# num_verify = 4

# for p in [np.random.rand() for _ in range(num_verify)]:
#     adj = pcomplete(N, pct=p)
#     weights = sum(adj[i][i] for i in range(N))
#     p_approx = (np.sum(adj) - weights) / (N ** 2)
#     print('actual:', round(p,4), '\tapprox:', round(p_approx, 4))

# write to outfile
write_adj(rbipart(N, pivot=N//2), '1.in')
write_adj(pcomplete(N, pct=0.5), '2.in')
write_adj(caliban(N, param=80), '3.in')
