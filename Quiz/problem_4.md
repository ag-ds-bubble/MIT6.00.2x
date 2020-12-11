# Quiz
## Problem 4
### You are given the following code. It has functions to create a random graph and to find a path between two nodes. The graph is represented by a dictionary; integer keys represent all the nodes in the graph; each key has a list of integers representing the nodes that the key has a directed edge to. Assume the code in the provided functions meets the specifications given.


```py
import random

# You are given this function - do not modify
def createRandomGraph():
    """Creates a digraph with 7 randomly chosen integer nodes from 0 to 9 and
    randomly chosen directed edges (between 10 and 20 edges)
    """
    g = {}
    n = random.sample([0,1,2,3,4,5,6,7,8,9], 7)
    for i in n:
        g[i] = []
    edges = random.randint(10,20)
    count = 0
    while count < edges:
        a = random.choice(n)
        b = random.choice(n)
        if b not in g[a] and a != b:
            g[a].append(b)
            count += 1
    return g

# You are given this function - do not modify
def findPath(g, start, end, path=[]):
    """ Uses DFS to find a path between a start and an end node in g.
    If no path is found, returns None. If a path is found, returns the
    list of nodes """
    path = path + [start]
    if start == end:
        return path
    if not start in g:
        return None
    for node in g[start]:
        if node not in path:
            newpath = findPath(g, node, end, path)
            if newpath: return newpath
    return None
                
#########################        
## WRITE THIS FUNCTION ##
#########################        

def allReachable(g, n):
    """
    Assumes g is a directed graph and n a node in g.
    Returns a sorted list (increasing by node number) containing all 
    nodes m such that there is a path from n to m in g. 
    Does not include the node itself.
    """
    #Get all nodes
    all_nodes = []
    connected_nodes = []
    for _ekey, _eval in g.items():
        all_nodes.append(_ekey)
        all_nodes += _eval
    all_nodes = list(set(all_nodes))
    for enode in [k for k in all_nodes if k!=n]:
        if findPath(g, n, enode) != None:
            connected_nodes.append(enode)
    return sorted(connected_nodes)

# allReachable(createRandomGraph(), 3)
```

### *You are not allowed to import anything. Do not leave any debugging print stataments. Click "See full output" to see the test cases passed/failed. Paste only the allReachable function and any helper functions you made for yourself (if any)*