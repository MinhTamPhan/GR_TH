from math import sqrt
class MyGraph(object):
	"""docstring for MyClass"""
	def __init__(self, arg):
		self.Matrix = arg[0]
		self.start = arg[1]
		self.gold = 0

	def isGold(self,v):
		n = len(self.Matrix)
		n = sqrt(n)
		if v / n == 0 or v / n == n - 1 or v % n == 0 or v % n == n-1:
			return True
		return False
	def dfs(self):
		stack = []
		stack.append(self.start)
		n = len(self.Matrix)
		label = [False for i in xrange(n)]
		previous = [-1 for i in xrange(n)]
		label[self.start] = True
		while len(stack) != 0:
			v = stack.pop()
			if self.isGold(v):
				self.gold = v
				return previous
			for i in xrange(n):
				if(self.Matrix[v][i] == 1 or self.Matrix[i][v] == 1):
					if(label[i] == False):
						previous[i] = v
						label[i] = True
						stack.append(i)
		return -1
	def printPath(self,path):
		n = len(self.Matrix)
		if path != -1:
			p = []
			i = self.gold
			print i
			p.append(i)
			while path[i] != -1:
				p.append(path[i])
				i = path[i]
				#print i
			p.reverse()
			print p
			for i in p:
				print "%d %d" %(i / sqrt(n), i % sqrt(n))
		else:
			print -1

from sys import argv
script, fileName = argv
textInput = open(fileName)
list1 = map(int, textInput.readline().strip().split())
n = int(list1[0])
Tunnel = []

for i in xrange(n):
	Tunnel.append(map(int, textInput.readline().strip().split()))
matrix = [[0 for i in xrange(n**2)] for i in xrange(n**2)]
for i in xrange(n**2):
	if i >= n and i < n**2 - n:
		if Tunnel[i / n][i % n] == 1 and Tunnel[i / n][i % n] == Tunnel[(i - n) / n][(i - n)%n]:
			matrix[i][i - n] = matrix[i - n][i] = 1
		if Tunnel[i / n][i % n] == 1 and Tunnel[i / n][i % n] == Tunnel[(i + n) / n][(i + n)%n]:
			matrix[i][i + n] = matrix[i + n][i] = 1
		if Tunnel[i / n][i % n] == 1 and Tunnel[i / n][i % n] == Tunnel[(i - 1) / n][(i - 1)%n]:
			matrix[i][i - 1] = matrix[i - 1][i] = 1
		if Tunnel[i / n][i % n] == 1 and Tunnel[i / n][i % n] == Tunnel[(i + 1) / n][(i + 1)%n]:
			matrix[i][i + 1] = matrix[i + 1][i] = 1
	if i < n or i >= n**2 - n:
		if Tunnel[i / n][i % n] == 1 and Tunnel[i / n][i % n] == Tunnel[(i - 1) / n][(i - 1)%n]:
			matrix[i][i - 1] = matrix[i - 1][i] = 1
		if Tunnel[i / n][i % n] == 1 and Tunnel[i / n][i % n] == Tunnel[(i + 1) / n][(i + 1)%n]:
			matrix[i][i + 1] = matrix[i + 1][i] = 1

# for i in xrange(n**2):
# 	print matrix[i]

argvc = []
argvc.append(matrix)
argvc.append(list1[1] * n + list1[2])

G = MyGraph(argvc)
p = G.dfs()
G.printPath(p)



			


		