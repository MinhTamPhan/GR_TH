from Graph import GRAPH
from sys import argv
script, fileInput, fileoutput, start, end = argv
start = int(start)
end = int (end)
def readFile(fileInput):
    """Read file Input """
    matrix = []
    f = open(fileInput)
    i = 0
    nVertex = 0;
    for lines in f:
        if i == 0:
            line = int(lines.strip())
            nVertex = line
        else:
            line = map(int, lines.strip().split('\t'))
            tmp = []
            tmp.extend(line)
            matrix.append(tmp)  
        i += 1  
    f.close()
    return nVertex, matrix


def InitAlorithmDijkstra (graph, start, end):
    """init Alortithm Dijktstra"""
    T = [1] * graph.getNumOfVertex()
    L = [-1] * graph.getNumOfVertex()
    Prev = [-1] * graph.getNumOfVertex()
    L[start] = 0
    return T, L, Prev

def DijkstraAlorithm(graph, start, end):
    """run Dijkstra Alorithm"""
    T , Length, Prev = InitAlorithmDijkstra(graph, start, end)
    n = graph.getNumOfVertex()
    matrix = graph.getMatrix()
    while T[end] == 1:
        iMin = -1
        v = -1		
        for i in range(n):
            if T[i] == 1 and Length[i] != -1 and (Length[i] < iMin or iMin == -1):
                iMin = Length[i]
                v = i
        print(T)
        if iMin == -1:
			#print ('Khong tim thay duong di')
            return False
        Length[v] = iMin
        T[v] = 0

        for j in range(n):
            if T[j] == 1 and int(matrix[v][j]) != 0:
                if Length[j] == -1 or Length[j] > Length[v] + int(matrix[v][j]):
                    Length[j] = Length[v] + int(matrix[v][j])
                    Prev[j] = int(v)
					#print(Prev)
    return Prev

def GetPath(start, end, Prev):
    """Show Path From Start to End"""
    k = end - 1
    rsl = []
    while k != -1:
        rsl += [k]
        k = Prev[k]
			#print (Prev)
        rsl += [start]	
    rsl.reverse()
    return rsl

n, m = readFile(fileInput)
g = GRAPH(n, m)
Prev = DijkstraAlorithm(g, start, end)
f = open(fileoutput, "w") 
if Prev == False:
    f.write ("-1")
else:
	p = GetPath(start, end, Prev)
	#l.write (l)
	for i in p:
		f.write(str(i) + ' ')