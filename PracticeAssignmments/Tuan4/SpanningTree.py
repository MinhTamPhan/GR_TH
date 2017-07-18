from MyGraph import *
from sys import *
from random import *
#Script, Alorithm, InputFile = argv

def ReadFile(InputFile):
    f = open(InputFile)
    NumOfVertex, NumOfEdge = map(int, f.readline().strip().split(' '))
    g = Graph()
    for lines in f:
        s, d, cost = map(int, lines.strip().split(' '))
        src = Node(s)
        dest = Node(d)
        if not g.has_node(src):
            g.add_node(src)
        if not g.has_node(dest):
            g.add_node(dest)
        edge = WeightedEdge(src, dest, cost)
        g.addEdge(edge)
    f.close()
    return NumOfVertex, NumOfEdge, g

#NumOfVertex, NumOfEdge, Graph = ReadFile(InputFile)
def PrimAlorithm(graph, NumOfEdge):
    SetVertexOfGrapth = list(graph.nodes)
    InitVertex = Node('0')
    SetVertexOfSpanningTree = [InitVertex]
    SetVertexOfGrapth.remove(InitVertex)

    EdgeSpanningTree = []
    TotalCost = 0
    while len(EdgeSpanningTree) < NumOfEdge - 1:
        MinCost = -1
        NextEdge = None
        for node in SetVertexOfSpanningTree:
            edgeOfNode = graph.get_edges_for_node(node)
            for edge in edgeOfNode:
                if edge.get_destination() in SetVertexOfGrapth:
                    if MinCost == -1 or MinCost > edge.get_total_cost():
                        MinCost = edge.get_total_cost()
                        NextEdge = edge
        if MinCost != -1:
            SetVertexOfSpanningTree += [NextEdge.get_destination()]
            SetVertexOfGrapth.remove(NextEdge.get_destination())
            EdgeSpanningTree += [NextEdge]
            TotalCost += MinCost
        else:
            print ('Graph not connected')
            return None, None
    return EdgeSpanningTree, TotalCost


# Sp , m = PrimAlorithm (Graph, NumOfVertex)
# if m != None:
#     print (m)
#     rsl = ''
#     for item in Sp:
#         rsl += (str(item) + ',')
#     print (rsl)
def ReadFileKrulkalAl(input):
    f = open(input)
    NumOfVertex, NumOfEdge = map(int, f.readline().strip().split(' '))
    g = []
    for lines in f:
        s, d, cost = map(int, lines.strip().split(' '))
        src = Node(s)
        dest = Node(d)
        edge = WeightedEdge(src, dest, cost)
        g += [edge]
    
    return sorted(g, key=WeightedEdge.get_total_cost)



def KrulkalAlorithm(edge):
    NumOfEdge = len(edge)
    SetEdgeOfSpanning = []
    SetVetexOfSpanning = []
    while len(SetEdgeOfSpanning) < NumOfEdge - 1:
        TopEdge = edge.pop(0)
        if TopEdge.get_source() in SetVetexOfSpanning:
            if TopEdge.get_destination() in SetVetexOfSpanning:
                continue
            else:
                SetEdgeOfSpanning += [TopEdge]
                SetVetexOfSpanning += [TopEdge.get_destination()]
        else:
            SetEdgeOfSpanning += [TopEdge]
            SetVetexOfSpanning += [TopEdge.get_source()]
            if TopEdge.get_destination() not in SetVetexOfSpanning:
                SetVetexOfSpanning += [TopEdge.get_destination()]
        print(SetEdgeOfSpanning)
        print (len(SetEdgeOfSpanning))
        # if len(edge) == 0:
        #     print ('do thi khong lien thong')
        #     return None
    return SetEdgeOfSpanning

edge = ReadFileKrulkalAl('E:\\01_Study\\01_Lap_Trinh\LearnGraphTheory\PracticeAssignmments\Tuan4\spanning_tree_tests\input1.txt')
T = KrulkalAlorithm (edge)
if T != None:
    rsl = ''
    for item in edge:
        rsl += (str(item) + ',')
    print (rsl)