from MyGraph import * 
from math import *
from sys import argv
script, inputfile, outputfile = argv

def ReadFile(FileName):
    f = open(FileName)
    x0, y0, x1, y1 =  map(int,f.readline().strip().split(' '))
    start = Node('('+ str(y0) + ', ' + str(x0) + ')')
    end = Node('('+ str(y1) + ', ' + str(x1) + ')')
    #print(start, end)
    NumOfVertex = int(f.readline())
    matrix = []
    m = f.readlines()
    for line in m:
        matrix += [list(map(int,line.strip().split(' ')))]
    g = Digraph()
    for i in range(NumOfVertex ** 2):
        src = Node('('+ str(i % NumOfVertex) +', '+ str(int(i / NumOfVertex)) + ')')
        top = i - NumOfVertex
        down = i + NumOfVertex
        left = i - 1
        right = i + 1
        if not g.has_node(src):
            g.add_node(src)
        
        if top >= 0 and matrix[int(top / NumOfVertex)][top % NumOfVertex] == 0:
            des = Node('('+ str(top % NumOfVertex) + ', ' + str(int(top / NumOfVertex)) + ')')
            if not g.has_node(des):
                g.add_node(des)
            # print('top', top)
            # print (src , des)
            g.add_edge(Edge(src, des))

        if int(down / NumOfVertex) < NumOfVertex and  matrix[int(down / NumOfVertex)][down % NumOfVertex] == 0:
            des = Node('('+ str(int(down % NumOfVertex)) +', '+ str(int(down / NumOfVertex)) + ')')
            if not g.has_node(des):
                g.add_node(des)
            # print('down', down)
            # print (src , des)
            g.add_edge(Edge(src, des))

        if int(right / NumOfVertex) < NumOfVertex and (right % NumOfVertex) != 0 and \
        matrix[int(right / NumOfVertex)][right % NumOfVertex] == 0:
            des = Node('('+ str(right % NumOfVertex) +', '+ str(int(right / NumOfVertex)) + ')')
            if not g.has_node(des):
                g.add_node(des)
            # print('right', right)
            # print (src , des)
            g.add_edge(Edge(src, des))   

        if left >= 0 and  matrix[int(left / NumOfVertex)][left % NumOfVertex] == 0:
            des = Node('('+ str(left % NumOfVertex) +', '+ str(int(left / NumOfVertex)) + ')')
            if not g.has_node(des):
                g.add_node(des)
            # print('left', left)
            # print (src , des)
            g.add_edge(Edge(src, des))  

    return g, start, end


def DepthFirstSearch(graph, start, end, currentPath):
    currentPath += [start]
    if start == end:
        return currentPath
    else:
        for child in graph.get_edges_for_node(start):
            if child not in currentPath:
                newPath = DepthFirstSearch(graph, child, end, currentPath)
                if newPath != None:
                    return newPath
        return None

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 

g, s, e = ReadFile(inputfile)
#print (g)
path = DepthFirstSearch(g, s, e,[])

print ('Depth First Search Alorithm: ')
if path != None:
    print(printPath(path))
else:
    print (-1)

def BreadthFirstSearch(graph, start, end):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    pathQueue = [start]
    label = [-1 for i in range(len(graph.nodes))]
    path = [Node('({}, {})'.format(-1, -1)) for i in range(len(graph.nodes))]
    NumOfVertex = int(sqrt(len(graph.nodes)))
    while len(pathQueue) != 0:
        #Get and remove oldest element in pathQueue
        lastNode = pathQueue.pop(0)
        if lastNode == end:
            return path, NumOfVertex
        for nextNode in graph.get_edges_for_node(lastNode):
            x, y = map(int,str(nextNode).strip('(),').split(','))
            if label[y * NumOfVertex + x] == -1:
                pathQueue += [nextNode]
                path[y * NumOfVertex + x] = lastNode
                label[y * NumOfVertex + x] = 0
    return None, None

def printBFS(path, start, end , n):
    p = [end]
    x, y = map(int,str(end).strip('(),').split(','))
    tmp = path[y * n + x]
    while tmp != start:
        p += [tmp]
        x, y = map(int,str(tmp).strip('(),').split(','))
        tmp = path[y * n + x]
    p += [start]
    p.reverse()
    result = ''
    for i in range(len(p)):
        result = result + str(p[i])
        if i != len(p) - 1:
            result = result + '->'
    return result 
path, n = BreadthFirstSearch (g, s, e)



print ('Breadth First Search Alorithm: ')
if path != None:
    print(printBFS(path, s, e, n))
else:
    print (-1)