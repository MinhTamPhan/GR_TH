class Graph(object):
	"""docstring for Graph"""
	def __init__(self, arg):
		self.NumberOfVertex = arg[0]
		self.Matrix = arg[1]
		self.LabelOfVertex = [0 for i in xrange(self.NumberOfVertex)]
		self.NumberOfConnected = 0

	"""Visited Vertex arugment using DFS Recursive"""
	def DFS_Visited_Recursive(self, Vertex, LabelOfVertex):
		self.LabelOfVertex[Vertex] = LabelOfVertex
		for i in xrange(self.NumberOfVertex):
			DFS_Visited_Recursive(self,	i , LabelOfVertex)

	"""Visited Vertex arugment using DFS not Recursive"""		
	def DFS_Visited(self, Vertex, LabelOfVertex):
		q = []
		q.append(Vertex)
		while len(q) > 0:
			v = q.pop()
			self.LabelOfVertex[v] = LabelOfVertex
			for i in xrange(self.NumberOfVertex):
				if(self.LabelOfVertex[i] == 0 and (self.Matrix[v][i] != 0 or self.Matrix[i][v] != 0)):
					q.append(i)

	def FindConnectedComponent(self):
			NumOfConnectedComponent = 0
			for i in xrange(self.NumberOfVertex):
				if (self.LabelOfVertex[i] == 0):
					NumOfConnectedComponent += 1
					self.DFS_Visited(i, NumOfConnectedComponent)
			return NumOfConnectedComponent

	def FindConnectedComponent_Recursive(self):
		NumOfConnectedComponent = 0
		for i in xrange(self.NumberOfVertex):
			if (self.LabelOfVertex[i] == 0):
				NumberOfConnected += 1
				DFS_Visited_Recursive(self, i, NumOfConnectedComponent)
		return NumOfConnectedComponent

	def PrintConnectedComponent(self):

		if(self.NumberOfConnected == 1):
			print "Do thi lien thong"
		else:
			print "Do thi lien thong, Co %d TPLT." % self.NumberOfConnected

			for i in xrange(1, self.NumberOfConnected + 1):
				print "Mien lien thong #%d" % i

				for j in xrange(self.NumberOfVertex):
					if self.LabelOfVertex[j] == i:
						print "%d" % j,
				print ""

def ReadInput(FileName):
	textInput = open(FileName)
	n = int(textInput.readline())
	matrix = []
	for i in xrange(n):
		matrix.append(map(int, textInput.readline().strip().split()))
	return n,matrix



from sys import argv
script, fileName = argv

arv = ReadInput(fileName)

g = Graph(arv)
g.NumberOfConnected = g.FindConnectedComponent()
g.PrintConnectedComponent()
