class GRAPH(object):
	"""docstring for GRAPH"""
	def __init__(self, nVertex, matrix):
		self.n = nVertex
		self.Matrix = matrix

	def getMatrix(self):
		return self.Matrix

	def getNumOfVertex(self):
		return self.n