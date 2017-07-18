import GraphConnected

from sys import argv
script, fileName = argv

def ReadInput(fileName):
	textInput = open(FileName)
	n,m = map(int, textInput.readline().strip().split())
	
	matrix = []
	for i in xrange(n):
		matrix.append(map(int, textInput.readline().strip().split()))

	n = n*m

	mapt = [[0 for i in xrange(n)] for i xrange(n)]

	for i in xrange(n):
		if i >= m and i < n - m:
			if matrix[i / m][i % m] == 1 and matrix[i / m][i % m] == matrix[(i - m) / m][(i - n)%m]:
				mapt[i][i - n] = mapt[i - n][i] = 1
			if matrix[i / m][i % m] == 1 and matrix[i / m][i % m] == matrix[(i + m) / n][(i + m)%m]:
				mapt[i][i + m] = mapt[i + m][i] = 1
			if matrix[i / m][i % m] == 1 and matrix[i / m][i % m] == matrix[(i - 1) / m][(i - 1)%m]:
				mapt[i][i - 1] = mapt[i - 1][i] = 1
			if matrix[i / m][i % m] == 1 and matrix[i / m][i % m] == matrix[(i + 1) / m][(i + 1)%m]:
				mapt[i][i + 1] = mapt[i + 1][i] = 1
		if i < m or i >= n - m:
			if matrix[i / m][i % m] == 1 and matrix[i / n][i % m] == matrix[(i - 1) / m][(i - 1)%m]:
				mapt[i][i - 1] = mapt[i - 1][i] = 1
			if matrix[i / m][i % m] == 1 and matrix[i / m][i % m] == matrix[(i + 1) / m][(i + 1)%m]:
				mapt[i][i + 1] = mapt[i + 1][i] = 1
	

arv = ReadInput(fileName)
