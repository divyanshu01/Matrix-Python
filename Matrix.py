class Matrix:
	matrix_list = []
	
	def inputMatrix(self):
		n = int(input("Enter number of rows for the matrix \n"))
		m = int(input("Enter number of columns for the matrix \n"))
		if n == m:
			for i in range(n):
				print("Enter row", (i + 1), "of matrix(elements seperated by space)")
				temp_list = []
				temp_list = input().split(" ")
				self.matrix_list.append(temp_list)
		else :
			print("The matrix is not a square matrix")
	
	def printMatrix(self):
		if len(self.matrix_list) != 0:
			for i in range(len(self.matrix_list)):
				for j in range(len(self.matrix_list[0])):
					print(self.matrix_list[i][j]," ", end="")
				print()
				
