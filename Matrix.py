import copy
class Matrix:

	def __init__(self):
		self.matrix_list = []
		self.no_of_row = 0
		self.no_of_col = 0
	
	def getMinor(self, matrix_list, j):
		#print("Entry:", matrix_list)
		matrix = copy.deepcopy(matrix_list)
		del matrix[0]
		for i in range(len(matrix)):
			del matrix[i][j]
		#print("After deletions", matrix_list)
		
		m = Matrix()
		m.matrix_list = matrix[:]
		m.no_of_row = len(m.matrix_list)
		m.no_of_col = len(m.matrix_list[0])
		x = m.detMatrix()
		#print(m.matrix_list, m.no_of_row, m.no_of_col)
		return x
	
	def detMatrix(self):
		if self.no_of_row == 2 and self.no_of_col == 2:
			return self.matrix_list[0][0] * self.matrix_list[1][1] - self.matrix_list[0][1] * self.matrix_list[1][0]
		else:
			det = 0
			for i in range(self.no_of_col):
				det += ((-1)**i) * self.matrix_list[0][i] * self.getMinor(self.matrix_list, i)
			return det
	
	def divScalarMatrix(self, scalar):
		if(scalar != 0):
			for i in range(self.no_of_row):
				for j in range(self.no_of_col):
					self.matrix_list[i][j] /= scalar
		else:
			print("Division not possible")
	
	def getMinorForCofactor(self, matrix_list, i, j):
		#print("Entry:", matrix_list)
		matrix = copy.deepcopy(matrix_list)
		del matrix[i]
		for k in range(len(matrix)):
			del matrix[k][j]
		#print("After deletions", matrix_list)
		
		m = Matrix()
		m.matrix_list = matrix[:]
		m.no_of_row = len(m.matrix_list)
		m.no_of_col = len(m.matrix_list[0])
		x = m.detMatrix()
		#print(m.matrix_list, m.no_of_row, m.no_of_col)
		return x
	
	def cofactorMatrix(self):
		if self.no_of_row == 2 and self.no_of_col == 2:
			return self.matrix_list[0][0] * self.matrix_list[1][1] - self.matrix_list[0][1] * self.matrix_list[1][0]
		else:
			det = 0
			cofactor = Matrix()
			for i in range(self.no_of_row):
				temp_list = []
				for j in range(self.no_of_col):
					value = ((-1)**(i + j)) * self.getMinorForCofactor(self.matrix_list, i, j);
					temp_list.append(value)
				cofactor.matrix_list.append(temp_list)
			
			cofactor.no_of_row = len(cofactor.matrix_list)
			cofactor.no_of_col = len(cofactor.matrix_list[0])
			
			return cofactor
	
	def inputMatrix(self):
		self.no_of_row = int(input("Enter number of rows for the matrix \n"))
		self.no_of_col = int(input("Enter number of columns for the matrix \n"))
		if self.no_of_row == self.no_of_col:
			for i in range(self.no_of_col):
				print("Enter row", (i + 1), "of matrix(elements seperated by space)")
				temp_list = []
				temp_list = input().split(" ")
				for i in range(len(temp_list)):
					temp_list[i] = int(temp_list[i])
				self.matrix_list.append(temp_list)
		else :
			print("The matrix is not a square matrix")
	
	def inverseMatrix(self):
		temp_list = copy.deepcopy(self.matrix_list)
		
		temp_matrix = Matrix()
		temp_matrix.matrix_list = temp_list
		temp_matrix.no_of_row = len(temp_list)
		temp_matrix.no_of_col = len(temp_list[0])
		det = temp_matrix.detMatrix()
		inverse = temp_matrix.cofactorMatrix()
		inverse.divScalarMatrix(det)
		
		return inverse
	
	def mulMatrix(self, m):
		if self.no_of_col == m.no_of_row:
			obj = Matrix()
			obj.no_of_row = self.no_of_row
			obj.no_of_col = m.no_of_col
			for i in range(self.no_of_row):
				temp_list = []
				for k in range(m.no_of_col):
					temp = 0
					for j in range(m.no_of_row):
						temp += self.matrix_list[i][j] * m.matrix_list[j][k]
					temp_list.append(temp)
				obj.matrix_list.append(temp_list)
			return obj
	
	def mulScalarMatrix(self, scalar):
		for i in range(self.no_of_row):
			for j in range(self.no_of_col):
				self.matrix_list[i][j] *= scalar
	
	def printMatrix(self):
		if len(self.matrix_list) != 0:
			for i in range(self.no_of_row):
				for j in range(self.no_of_col):
					print(self.matrix_list[i][j]," ", end="")
				print()
		else:
			print("Matrix is empty yet")
				
	def addMatrix(self, mat):
		if self.no_of_row == mat.no_of_row:
			if self.no_of_col == mat.no_of_col:
				m = Matrix()
				m.no_of_row = self.no_of_row
				m.no_of_col = self.no_of_col
				print(m.matrix_list)
				for i in range(self.no_of_row):
					temp_list = []
					for j in range(self.no_of_col):
						temp_list.append(self.matrix_list[i][j] + mat.matrix_list[i][j])
					m.matrix_list.append(temp_list)
				return m
			else:
				print("Number of columns are not equal")
		else:
			print("Number of rows are not equal")

	def subMatrix(self, mat):
		if self.no_of_row == mat.no_of_row:
			if self.no_of_col == mat.no_of_col:
				m = Matrix()
				m.no_of_row = self.no_of_row
				m.no_of_col = self.no_of_col
				print(m.matrix_list)
				for i in range(self.no_of_row):
					temp_list = []
					for j in range(self.no_of_col):
						temp_list.append(self.matrix_list[i][j] - mat.matrix_list[i][j])
					m.matrix_list.append(temp_list)
				return m
			else:
				print("Number of columns are not equal")
		else:
			print("Number of rows are not equal")
	
	def transMatrix(self):
		for i in range(self.no_of_row):
			for j in range(self.no_of_col):
				if i > j:
					self.matrix_list[i][j], self.matrix_list[j][i] = self.matrix_list[j][i], self.matrix_list[i][j]
	
	
	def getMinorForCofactor(self, matrix_list, i, j):
		#print("Entry:", matrix_list)
		matrix = copy.deepcopy(matrix_list)
		del matrix[i]
		for k in range(len(matrix)):
			del matrix[k][j]
		#print("After deletions", matrix_list)
		
		m = Matrix()
		m.matrix_list = matrix[:]
		m.no_of_row = len(m.matrix_list)
		m.no_of_col = len(m.matrix_list[0])
		x = m.detMatrix()
		#print(m.matrix_list, m.no_of_row, m.no_of_col)
		return x
	
	def getCofactorMatrix(self):
		if self.no_of_row == 2 and self.no_of_col == 2:
			return self.matrix_list[0][0] * self.matrix_list[1][1] - self.matrix_list[0][1] * self.matrix_list[1][0]
		else:
			det = 0
			for i in range(self.no_of_row):
				for j in range(self.no_of_col):
					det += ((-1)**(i + j)) * self.getMinorForCofactor(self.matrix_list, i, j);
			return det
