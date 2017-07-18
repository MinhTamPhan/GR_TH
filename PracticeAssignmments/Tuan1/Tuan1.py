from MyGraph import *
from sys import argv
script, option, inputfile, outputfile = argv

def ReadFile(File):
    if option == '1':
        f = open(File)
        i = 0
        n = 0
        matrix = []
        for lines in f:
            if i == 0:
                n = int(lines)
            else:
                matrix += [list(map(int,lines.strip().split(' ')))]
            i += 1
        return Graph(n, matrix)
    else:
        f = open(File)
        n, e = 0, 0
        i = 0
        g = Digraph()
        for lines in f:
            if i == 0:
                n, e = map(int,lines.strip().split(' '))
            else:
                v1 , v2 = map(int,lines.strip().split(' '))
                Source = Node(v1)
                Des = Node(v2)
                #print (Source, Des)
                if not g.has_node(Source):
                    g.add_node(Source)
                if not g.has_node(Des):
                    g.add_node(Des)
                g.add_edge(Edge(Source, Des))
                
            i += 1
        return g
g = ReadFile(inputfile)
#print(g.Matrix)