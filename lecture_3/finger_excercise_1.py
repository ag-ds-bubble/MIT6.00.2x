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
        self.mapDF = pd.DataFrame(columns=['source','target'])
        idx = 0
        for esrc in self.edges:
            for edst in self.edges[esrc]:
                self.mapDF.loc[idx, 'source'] = esrc.getName()
                self.mapDF.loc[idx, 'target'] = edst.getName()
                idx+=1

        G=nx.from_pandas_edgelist(self.mapDF)
        nx.draw_networkx(G, with_labels=True, arrows = True, arrowstyle = '>')
        plt.grid()
        plt.show()

        return 'Digraph'
    
    def __repr__(self):
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
        self.mapDF = pd.DataFrame(columns=['source','target'])
        idx = 0
        for esrc in self.edges:
            for edst in self.edges[esrc]:
                self.mapDF.loc[idx, 'source'] = esrc.getName()
                self.mapDF.loc[idx, 'target'] = edst.getName()
                idx+=1
        G=nx.from_pandas_edgelist(self.mapDF)
        nx.draw_networkx(G, with_labels=True)
        plt.grid()
        plt.show()
        return 'UndirectedGraph'

    def __repr__(self):
        return 'UndirectedGraph'

def buildLine(GraphType):
    g = GraphType()
    # Add Nodes
    for perms in ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']:
        g.addNode(Node(perms))

    # Add Edges
    if GraphType().__repr__() == 'Digraph':
        g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
        g.addEdge(Edge(g.getNode('ABC'), g.getNode('BAC')))

        g.addEdge(Edge(g.getNode('ACB'), g.getNode('ABC')))
        g.addEdge(Edge(g.getNode('ACB'), g.getNode('CAB')))

        g.addEdge(Edge(g.getNode('BAC'), g.getNode('BCA')))
        g.addEdge(Edge(g.getNode('BAC'), g.getNode('ABC')))

        g.addEdge(Edge(g.getNode('BCA'), g.getNode('CBA')))
        g.addEdge(Edge(g.getNode('BCA'), g.getNode('BAC')))
        
        g.addEdge(Edge(g.getNode('CAB'), g.getNode('ACB')))
        g.addEdge(Edge(g.getNode('CAB'), g.getNode('CBA')))
        
        g.addEdge(Edge(g.getNode('CBA'), g.getNode('CAB')))
        g.addEdge(Edge(g.getNode('CBA'), g.getNode('BCA')))

    elif GraphType().__repr__() == 'UndirectedGraph':
        g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
        g.addEdge(Edge(g.getNode('ABC'), g.getNode('BAC')))

        g.addEdge(Edge(g.getNode('ACB'), g.getNode('CAB')))

        g.addEdge(Edge(g.getNode('BAC'), g.getNode('BCA')))

        g.addEdge(Edge(g.getNode('CBA'), g.getNode('CAB')))
        g.addEdge(Edge(g.getNode('CBA'), g.getNode('BCA')))

    return g


dg = buildLine(Digraph)
print(dg)
dg = buildLine(Graph)
print(dg)
