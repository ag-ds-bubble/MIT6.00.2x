import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, name, index):
        self.name = name
        self.index = index
    def __str__(self):
        return f'{self.index}. '+self.name
    def __repr__(self):
        return f'{self.index}. '+self.name
    def getName(self):
        return self.name
    def getIndex(self):
        return self.index

class Edge:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.desc = self.src.getName() + '->' + self.dst.getName()
    def __str__(self):
        return self.desc
    def __repr__(self):
        return self.desc
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dst
            
class Digraph(object):
    def __init__(self):
        self.edges={}
        
    def __str__(self):
        G = nx.DiGraph()
        for esrc in self.edges:
            G.add_node(esrc)
        for esrc in self.edges:
            for edst in self.edges[esrc]:
                G.add_edge(esrc, edst)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color='k', arrows = True)
        plt.show()
        return 'Digraph'

    def __repr__(self):
        return 'Digraph'

    def addNode(self, node):
        if node not in self.edges:
            self.edges[node] = []
        else:
            raise ValueError(f"{node} already avaialable in the graph")

    def getNode(self, node_name):
        for enode in self.edges:
            if enode.getName() == node_name:
                return enode
        return f"No {node_name} found in the graph"

    def addEdge(self, edge):
        src = edge.getSource()
        dst = edge.getDestination()
        if not (src in self.edges and dst in self.edges):
            raise ValueError("Node not in the Graph")
        self.edges[src].append(dst)

    def childrenOf(self, node):
        return sorted(self.edges[node], key=lambda x : x.getIndex(), reverse=False)

    @staticmethod
    def printdfs(npath):
        res = ''
        for enode in npath:
            res += enode.getName()+'->'
        print(res)
        
    @staticmethod
    def DFS(graph, start, end, path, shortest, toPrint=False):
        path+=[start]
        if start == end:
            return path
        for childNode in graph.childrenOf(start):
            if toPrint : Digraph.printdfs(path)
            if childNode not in path:
                if shortest == None or len(path) < len(shortest):
                    newPath = Digraph.DFS(graph, childNode, end, path, shortest, toPrint)
                    if newPath != None:
                        shortest = newPath
            elif toPrint:
                print('Visited', childNode, 'earlier')
        return shortest

    def getShortestPath(self, node1, node2, _print=True, mode='BFS'):
        res = ''
        if mode=='BFS':
            spath = self.DFS(self, node1, node2, [], None, _print)
        for k in spath:
            res += str(k.getIndex())
        print(res)
        return res

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

    def __str__(self):
        G = nx.DiGraph()
        for esrc in self.edges:
            G.add_node(esrc)
        for esrc in self.edges:
            for edst in self.edges[esrc]:
                G.add_edge(esrc, edst)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color='k', arrows = True)
        plt.show()
        return 'UndirectedGraph'

    def __repr__(self):
        return 'UndirectedGraph'

def buildLine(GraphType):
    g = GraphType()
    # Add Nodes
    for pidx, perms in enumerate(['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']):
        g.addNode(Node(perms, pidx))

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

dg = buildLine(Graph)
dg.getShortestPath(dg.getNode('BCA'), dg.getNode('ACB'))
