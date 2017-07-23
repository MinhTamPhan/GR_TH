from MyGraph import *
from sys import *
Script, Input, Output = argv

def ReadFile(InputFile):
    f = open(InputFile)
    Martrix = []
    for line in f:
        Martrix += [list(map(int, line.strip().split()))]
    #print(Martrix)
    f.close()
    return Martrix

def InitGraph(matrix):
    """init graph and deny color for each vertex"""
    NumOfColored = 0
    g = Graph()
    deny_color = {}
    color = {}
    for i in range(9**2):
        node = Node(i)
        g.add_node(node)
        deny_color[node] = []
    row , col = 0, 0
    for i in range(9):
        for j in range(9):
            if matrix[i][j] != 0:
                NumOfColored += 1
                color[Node(i * 9 + j)] = matrix[i][j]
            row = (i // 3) * 3
            col = (j // 3) * 3
            CurrentNode = Node(i * 9 + j)
            list_edge = []
            for tmp in range(9):
                src = Node(i * 9 + tmp)
                edge = Edge(src, CurrentNode)
                if tmp != j:
                    if matrix[i][j] == 0:
                        list_edge += [edge]
                    else:
                        if matrix[i][j] not in deny_color[src]:
                            deny_color[src] += [matrix[i][j]]
                src = Node(tmp * 9 + j)
                edge = Edge(src, CurrentNode)
                if tmp != i:
                    if matrix[i][j] == 0:
                        list_edge += [edge]
                    else:
                        if matrix[i][j] not in deny_color[src]:
                            deny_color[src] += [matrix[i][j]]
            for rblock in range(row, row + 3):
                for cblock in range(col, col + 3):
                    if rblock != i and cblock != j:
                        src = Node(rblock * 9 + cblock)
                        edge = Edge(src, CurrentNode)                      
                        if matrix[i][j] == 0:
                            list_edge += [edge]
                        else:
                            if matrix[i][j] not in deny_color[src]:
                                deny_color[src] += [matrix[i][j]]
            for edge in list_edge:
                g.add_edge(edge)
    #print(color)
    return g, deny_color, NumOfColored, color

def Coloring_Algorithm(graph, deny_color, NumOfColored, color):
    def FindMaxLevelVertex(graph, color, deny_color):
        MaxLv = 0
        ResultNode = None
        for node in graph.get_nodes():
            if node not in color.keys():# don't have color
                if len(deny_color[node]) > MaxLv: #find node have number of colored max
                    MaxLv = len(deny_color[node])
                    ResultNode = node
        return ResultNode
    def ChoiceColer(graph, deny_color , CurrentNode):
        Color = [0] * 10
        colori = 0
        for i in range(1, 10):
            if i not in deny_color[CurrentNode]:
                for edge in graph.get_edges_for_node(CurrentNode):
                    if i in deny_color[edge.get_destination()]:
                        Color[i] += 2
                    else:
                        Color[i] += 1
        for i in Color:
            if i == max(Color):
                print (colori)
                return colori
            colori += 1
        return 0
    while NumOfColored < 81:
        NumOfColored += 1
        node = FindMaxLevelVertex(graph, color, deny_color)
        c = ChoiceColer(graph, deny_color, node)
        if c == 0:
            print("Khong tim duoc loi giai")
            print(color)
            return None
        color[node] = c
        for no in graph.get_edges_for_node(node):
            if c not in deny_color[no.get_destination()]:
                deny_color[no.get_destination()] += [c]
    print(color)
    return color

matrix = ReadFile(Input)
graph, deny_color, NumOfColored, color = InitGraph (matrix)
color = Coloring_Algorithm(graph, deny_color, NumOfColored, color)
txtOutput = []
f = open(Output)
for line in f:
    txtOutput += [list(map(int, line.strip().split()))]

def CheckOutput(color, txtOutput):
    for i in range(9):
        for j in range(9):
            if (color[Node(i * 9 + j)] != txtOutput[i][j]):
                print("Loi giai sai")
                return
    print("Exactly!!! :)")
if color != None:
    CheckOutput(color, txtOutput)