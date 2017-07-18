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

# listEdge = []

# def InitListEdge(listEdge):
# 	for i in xrange(graph.NumberOfVertex):
# 		for j in xrange(graph.NumberOfVertex):
# 			if (graph.Matrix[i][j] != 0):
# 				edge = EDGE()
# 				edge.v1 = i
# 				edge.v2 = j
# 				edge.w = graph.Matrix[i][j]
# 				listEdge.append(edge)

# def SortListEdge():
# 	return listEdge.sort()

def isCircle(index, label, listEdge):
	if(label[listEdge[index].v1] == label[listEdge[index].v2]):
		return True
	else:
		label1 = 0
		label2 = 0
		if(label[listEdge[index].v1] > label[listEdge[index].v2]):
			label1 = label[listEdge[index].v2]
			label2 = label[listEdge[index].v1]
		else:
			label1 = label[listEdge[index].v1]
			label2 = label[listEdge[index].v2]
		for i in xrange(len(label)):
			if(label[i] == label2):
				label[i] = label1

	return False

def KruskalAlgorithm(listEdge,NumberOfVertex):
	T = []
	nT = 0
	nV = NumberOfVertex
	label = []
	for i in xrange(nV):
		label.append(i)
	minIndex = 0
	listEdge.sort(None,key=lambda e : e.getKey())   
	nlist = len(listEdge)
	while nT < nV - 1:
		if minIndex < nlist:
			if not isCircle(minIndex,label,listEdge):
				T.append(listEdge[minIndex])
				nT += 1
			minIndex += 1
		else:
			print "Do Thi Khong Lien Thong"

	ShowTree(T)


def ReadInput(fileName):
	textInput = open(fileName)
	n,m = textInput.readline().strip().split()
	n = int(n)
	m = int(m)
	l = []
	for i in xrange(m):
		e = EDGE()
		e.v1,e.v2,e.w = textInput.readline().strip().split()
		e.v1 = int(e.v1)
		e.v2 = int(e.v2)
		e.w = int(e.w)
		l.append(e)

	return l,n


from sys import argv
script, fileName = argv




l,n = ReadInput(fileName)

KruskalAlgorithm(l,n)
