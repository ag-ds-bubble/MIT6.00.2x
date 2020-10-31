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
        nx.draw(G, with_labels=True)
        plt.grid()
        plt.show()

        return ''

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
print(dg)
# print(buildCityGraph(Graph))



# Visualise a Graph


