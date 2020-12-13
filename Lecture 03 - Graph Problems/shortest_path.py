import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


class Node:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName()+'->'+self.dest.getName()

class Digraph(object):
    def __init__(self):
        self.edges = {}

    def __str__(self):
        G = nx.DiGraph(directed=True)
        # Add all the nodes to the graph        
        for esrc in self.edges:
            G.add_node(esrc)
        # Add Edges
        for esrc in self.edges:
            for edst in self.edges[esrc]:
                G.add_edge(esrc, edst)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color='k', arrows = True)
        plt.show()
        return 'Digraph'

    def addNode(self, node):
        if node in self.edges:
            raise ValueError("Duplicate Node")
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dst = edge.getDestination()
        if not (src in self.edges and dst in self.edges):
            raise ValueError("Node not in the Graph")
        self.edges[src].append(dst)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        return NameError(name)

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

    def __str__(self):
        G = nx.DiGraph()
        # Add all the nodes to the graph        
        for esrc in self.edges:
            G.add_node(esrc)
        # Add Edges
        for esrc in self.edges:
            for edst in self.edges[esrc]:
                G.add_edge(esrc, edst)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color='k', arrows = True)
        plt.show()

        return 'UndirectedGraph'


def buildCityGraph(GraphType):
    g = GraphType()
    # Add Nodes
    for cityName in ['Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles']:
        g.addNode(Node(cityName))

    # Add Edges
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))

    return g

dg = buildCityGraph(Digraph)

def printDFS(paths, shortest_sofar):
    sres = ''
    if shortest_sofar:
        sres = f'Length of the shortest path so far {len(shortest_sofar)}'
    if paths:
        res = 'Currently visiting : '
        for enode in paths:
            res += enode.getName() +'->'
        print(res+'\t'+sres)

def printBFS(paths):
    res = ''
    if paths:
        for enode in paths:
            res += enode.getName()+'->'
    return res



def DFS(graph, start, end, path, shortest, toPrint=True):
    path = path + [start]
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if toPrint:
            printDFS(path+[node], shortest)
        if node not in path: # Avoid for cycles
            if shortest == None or len(path) < len(shortest):
                newpath = DFS(graph, node, end, path, shortest, toPrint)
                if newpath != None:
                    shortest = newpath
        else:
            if toPrint:
                print('Visited', node, 'earlier')
    return shortest


def BFS(graph, start, end, toPrint=True):
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path :', printBFS(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath: # Check if its already in the path
                newPath = tmpPath+[nextNode]
                pathQueue.append(newPath)
    return None


def shortestPathDFS(graph, start, end, toPrint=True):
    spath = DFS(graph, start, end, [], None, toPrint)
    res = ''
    if spath:
        for eidx, enode in enumerate(spath):
            res += enode.getName()+'-->\n'+'\t'*(eidx+1)
        print(res)
    else:
        print('No shortest path found!')

def shortestPathBFS(graph, start, end, toPrint=True):
    spath = BFS(graph, start, end, toPrint)
    res = ''
    if spath:
        for eidx, enode in enumerate(spath):
            res += enode.getName()+'-->\n'+'\t'*(eidx+1)
        print(res)
    else:
        print('No shortest path found!')

# shortestPathDFS(dg, dg.getNode('Los Angeles'), dg.getNode('Denver'))
# shortestPathDFS(dg, dg.getNode('Chicago'), dg.getNode('Boston'), False)
# shortestPathDFS(dg, dg.getNode('Boston'), dg.getNode('Phoenix'), True)

# shortestPathBFS(dg, dg.getNode('Chicago'), dg.getNode('Boston'), True)
# shortestPathBFS(dg, dg.getNode('Boston'), dg.getNode('Phoenix'), True)

print(dg)

