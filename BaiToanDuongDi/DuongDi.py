from sys import argv
script, fileName = argv

class GRAPH(object):
	"""docstring for GRAPH"""
	def __init__(self, nVertex, matrix):
		self.n = nVertex
		self.Matrix = matrix

	def getMatrix(self):
		return self.Matrix

	def getNumOfVertex(self):
		return self.n


def readFile(fileName):
	f = open(fileName)
	n = 0
	start , end = 0 , 0
	i = 0
	matrix = []
	for line in f:
		if i == 0:
			n = line
		elif i == 1:
			start, end = line.strip().split(' ')
		else:
			k = line.strip().split(' ')
			t = []
			for j in k:
				t += [int(j)]
			matrix += [t]
		i += 1
	return int(start), int(end) , matrix


def initAlorithmDijkstra (graph, start, end):
	T = [1] * graph.getNumOfVertex()
	L = [-1] * graph.getNumOfVertex()
	Prev = [-1] * graph.getNumOfVertex()
	L[start] = 0
	return T, L, Prev




def Dijkstra(graph, start, end):
	T , Length, Prev = initAlorithmDijkstra(graph, start, end)
	n = graph.getNumOfVertex()
	matrix = graph.getMatrix()
	while T[end] == 1:
		iMin = -1
		v = -1		
		for i in range(n):
			if T[i] == 1 and Length[i] != -1 and (Length[i] < iMin or iMin == -1):
				iMin = Length[i]
				v = i
		#print (T)
		if iMin == -1:
			print ('Khong tim thay duong di')
			return False
		Length[v] = iMin
		T[v] = 0

		for j in range(n):
			if T[j] == 1 and int(matrix[v][j]) != 0:
				if Length[j] == -1 or Length[j] > Length[v] + int(matrix[v][j]):
					Length[j] = Length[v] + int(matrix[v][j])
					Prev[j] = int(v)
					#print(Prev)

	def ShowPath(start, end, Prev):
		k = end - 1
		rsl = ''
		while k != 0:
			rsl += (str(k + 1) + '<----')
			k = Prev[k]
			#print (Prev)
		rsl += str(start)	
		print (rsl)	
	ShowPath(s, e,Prev)
	print ('Min Length Path: ', Length[end])
	return True

s, e, m = readFile(fileName)
g = GRAPH(len(m), m)
Dijkstra (g, s - 1, e - 1)