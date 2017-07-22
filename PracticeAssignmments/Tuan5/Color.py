from MyGraph import *
from sys import *
from random import *
Script, Algorithm, InputFile, output = argv

def ReadFile(InputFile):
    f = open(InputFile)
    NumOfVertex, NumOfEdge = map(int, f.readline().strip().split(' '))
    g = Graph()
    for lines in f:
        s, d = map(int, lines.strip().split(' '))
        src = Node(s)
        dest = Node(d)
        if not g.has_node(src):
            g.add_node(src)
        if not g.has_node(dest):
            g.add_node(dest)
        edge = Edge(src, dest)
        #print (edge)
        g.addEdge(edge)
    f.close()
    return NumOfVertex, NumOfEdge, g




def coloring(graph, NumOfVertex):
    colored = []
    deny_color = {}
    color = {}
    coutcolor = 0;
    """init dictionary node with list color deny allow"""
    for i in graph.get_nodes():
        deny_color[i] = []
    
    def FindMaxlever(graph):
        MaxNode = None
        MaxVertex = -1
        for node in graph.get_nodes():
            if MaxVertex == -1 or MaxVertex < graph.get_level(node):
                if node not in colored:
                    MaxNode = node
                    MaxVertex = graph.get_level(node)
        return MaxNode, MaxVertex

    while len(color.keys()) < NumOfVertex:
        node, lv = FindMaxlever(graph)
        # print(node, lv)
        # print(color.keys())
        for i in range(255):
            if i not in deny_color[node]:
                color[node] = i
                if i > coutcolor:
                    coutcolor = i
                for edge in graph.get_edges_for_node(node):
                    rev = Edge(edge.dest, edge.src)
                    #print(rev)
                    #print(str(graph.edges[rev.src]))
                    graph.remove_edge(rev)
                    deny_color[edge.dest] += [i]
                graph.remove_all_edge(node)
                colored += [node]
                break
        if(len(deny_color[node]) == 255):
            return -1, None
    return color, coutcolor



def GreendyAlorithm(Graph, NumOfVertex):
    color = {}
    colori = {}
    counter = 0
    nodes = Graph.get_nodes()
    for i in range(255):
        colori[i] = []
        for n in nodes:
            if n not in color.keys():
                if(n not in colori[i]):
                    color[n] = i
                    for child in Graph.get_edges_for_node(n):
                        colori[i] += [child.get_destination()]     
        counter += 1
        if (len(color.keys()) == NumOfVertex):
            return color, counter          
    if(len(color.keys()) > 255):
        return color, -1
    return -1

NumOfVertex, NumOfEdge, Graph = ReadFile(InputFile)

if Algorithm == 'Greendy':
    color, count = GreendyAlorithm(Graph, NumOfVertex)
else:
    color, count = coloring(Graph, NumOfVertex)

def pr(color):
    edge_strs = []
    for k in color.keys():
        edge_strs.append('{} {}'.format(k,color[k]))
    edge_strs = sorted(edge_strs)  # sort alphabetically
    return '\n'.join(edge_strs)  # concat edge_strs with "\n"s between them

if count != -1:
    print (pr(color))
    print('so mau phai to: {}'.format(count))
else:
    print(color)