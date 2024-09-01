# the commenly used initialization in graph algorithms
def initialize(adj,s):
    infinity = float('inf')         # number greater than sum of all + weights
    d = [infinity for _ in adj]     # shortest path estimates d(s, v)
    parent = [None for _ in adj]    # initialize parent pointers
    d[s], parent[s] = 0, s          # initialize source
    return d, parent