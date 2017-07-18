from sys import exit
class EDGE(object):
	"""Class store two verties v1 and v2 and has weight = w"""
	def __init__(self):
		self.v1 = None
		self.v2 = None
		self.w = None

	def getKey(self):
		return self.w

class Graph(object):
	"""docstring for Graph"""
	def __init__(self, arg):
		self.NumberOfVertex = arg[0]
		self.Matrix = arg[1]

def ShowTree(edge):
	"""Show Spaning Tree"""
	nE = len(edge)
	iWeight = 0
	for i in xrange(nE):
		iWeight += edge[i].w
	"""Print Spaning Tree"""
	print "Trong luong cay khung nho nhat: %d" % iWeight
	print "Danh sach cac canh trong cay khung"
	"""print list edge in spanning tree"""
	for i in xrange(nE):
		print("(%d, %d)" % (edge[i].v1 ,edge[i].v2))

def PrimAlgorithm(graph):
	"""Implement Alogorithm Prim"""
	# initial all element of labels isn't visited
	T = [] # list Edge
	nT = 0 # size list Edge

	labels = [] # list label check is Visited


	for i in xrange(graph.NumberOfVertex):
		labels.append(False)

	labels[0] = True

	while(nT < graph.NumberOfVertex - 1):
		emin = EDGE()
		iMinWeight = -1 # -1 mean is not min Edge
		# thought all vertex is not visited
		for i in xrange(graph.NumberOfVertex):
			if labels[i] == False:
				# thought all vertex is visited
				for j in xrange(graph.NumberOfVertex):
					if labels[j] == True and graph.Matrix[i][j] != 0:
						if iMinWeight == -1 or iMinWeight > graph.Matrix[i][j]:
							emin.v1 = j
							emin.v2 = i
							emin.w = g.Matrix[i][j]
							iMinWeight = g.Matrix[i][j]

		if iMinWeight == -1:
			print "Do thi khong lien thong"
		else:
			T.append(emin)
			labels[emin.v2] = True
			nT += 1

	return T

def ReadInput(FileName):
	textInput = open(FileName)
	n,m = textInput.readline().strip().split()
	n = int(n)
	m = int(m)

	matrix = [[0 for i in xrange(n)] for i in xrange(n)]
	for i in xrange(m):
		tmp = map(int, textInput.readline().strip().split())
		matrix[tmp[0]][tmp[1]] = tmp[2]
		matrix[tmp[1]][tmp[0]] = tmp[2]

	#print matrix
	return n,matrix

from sys import argv
script, fileName = argv




arv = ReadInput(fileName)
g = Graph(arv)

T = PrimAlgorithm(g)
ShowTree(T)