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
    def __init__(self, src, dest, weight=0):
        self.src = src
        self.dest = dest
        self.weight = weight

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest
        
    def getWeight(self):
        return self.weight

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
            for edst, edwt in self.edges[esrc]:
                G.add_edge(esrc, edst, weight=edwt)
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G,'weight')

        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color='k', arrows = True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        
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
        weight = edge.getWeight()
        if not (src in self.edges and dst in self.edges):
            raise ValueError("Node not in the Graph")
        self.edges[src].append((dst, weight))

    def childrenOf(self, node):
        return [k[0] for k in self.edges[node]]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        return NameError(name)

    def getWeightBetween(self, nodeS, nodeD):
        for edst, edst_wt in self.edges[nodeS]:
            if edst == nodeD:
                return edst_wt

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
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence'), weight=5))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York'), weight=10))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston'), weight=12))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York'), weight=2))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago'), weight=20))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver'), weight=16))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix'), weight=30))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix'), weight=9))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York'), weight=23))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston'), weight=32))

    return g

def _printDFS(graph, paths, shortest_sofar):
    sres = ''
    if shortest_sofar:
        sres = f'Weight of the shortest path so far {_get_path_weights_sum(graph, shortest_sofar)}'
    if paths:
        res = 'Currently visiting : '
        for enode in paths:
            res += enode.getName() +'->'
        print(res+f' Current Weight : {_get_path_weights_sum(graph, paths)}'+'\t'+sres)

def _get_path_weights_sum(g, pathList):
    _sum = 0
    for src, dst in zip(pathList[:-1], pathList[1:]):
        _sum+=g.getWeightBetween(src, dst)
    return _sum

def DFS(graph, start, end, path, shortest, toPrint=True, weighted=False):
    path = path + [start]
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if toPrint:
            _printDFS(graph, path+[node], shortest)
        if node not in path: # Avoid for cycles
            # Check for weighted or len based on the `weighted` argument
            check = False
            if shortest:
                if weighted:
                    check = _get_path_weights_sum(graph, path) > _get_path_weights_sum(graph, shortest)
                else:
                    print('here')
                    check = len(path) < len(shortest)
            if shortest == None or check:
                newpath = DFS(graph, node, end, path, shortest, toPrint, weighted)
                if newpath != None:
                    shortest = newpath
        else:
            if toPrint:
                print('Visited', node, 'earlier')
    return shortest

def shortestPathDFS(graph, start, end, toPrint=True, weighted=False):
    spath = DFS(graph, start, end, [], None, toPrint, weighted)
    res = ''
    if spath:
        for eidx, enode in enumerate(spath):
            res += enode.getName()+'-->\n'+'\t'*(eidx+1)
        print(res)
    else:
        print('No shortest path found!')


dg = buildCityGraph(Digraph)
shortestPathDFS(dg, dg.getNode('Boston'), dg.getNode('Phoenix'), True, True)
print(dg)

