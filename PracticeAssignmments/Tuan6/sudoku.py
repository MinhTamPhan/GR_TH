from MyGraph import *
from sys import *
Script, Input, Output = argv

def ReadFile(InputFile):
    f = open(InputFile)
    Martrix = []
    for line in f:
        Martrix += [list(map(int, line.strip().split()))]
    #print(Martrix)
    return Martrix

def InitGraph(matrix):
    """init graph and deny color for each vertex"""
    NumOfColored = 0
    g = Graph()
    for i in range(9**2):
        g.add_node(Node(i))
    row , col = 0, 0
    for i in range(9):
        for j in range(9):
            row = i // 3
            col = j // 3
            for node in matrix[i]:
                if matrix[i][j] != node:
                    src = Node(matrix[i][j])
                    if matrix[i][j] == 0:
                        g.add_edge(Edge(src, node))
                    else:
                        g.add_edge(Edge(node, src))
            if(matrix[i][j] != 0):
                NumOfColored += 1
            


ReadFile(Input)
print (4//3)