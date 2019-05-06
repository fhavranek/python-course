#! /usr/bin/env python3

import copy
import sys

class Matrix:
	def __init__(self, rows, columns):
		self.row_count = rows
		self.column_count = columns
		self.rows = {}
		self.columns = {}
	def check_index(self, row, column):
		if (row <= 0 or row > self.row_count or column <=0 or column > self.column_count):
			print(row, column)
			self.print()
			raise IndexError("Index out of matrix.")
	def set(self, row, column, number):	# counted form 1
		self.check_index(row, column)
		if str(row) in self.rows:
			self.rows[str(row)][str(column)] = number
		else:
			c = {str(column) : number}
			self.rows[str(row)] = c
		if str(column) in self.columns:
			self.columns[str(column)][str(row)] = number
		else:
			r = {str(row) : number}
			self.columns[str(column)] = r
	def read(self, row, column):
		self.check_index(row, column)
		if (str(row) in self.rows and str(column) in self.rows[str(row)]):
			return self.rows[str(row)][str(column)]
		else:
			return 0
	def print(self):
		for i in range(1, self.row_count+1):
			for j in range(1, self.column_count+1):
				print(self.read(i, j), end = " ")
			print()
		print()

	def __add__(self, other):
		if (self.row_count != other.row_count or self.column_count != other.column_count):
			print("Cannot add different dimensions of matrices", file = sys.stderr)
		else:
			m = copy.deepcopy(self)
			for i in range(1, other.row_count+1):
				for j in range(1, other.column_count+1):
					m.set(i, j, self.read(i, j) + other.read(i, j))
			return m

	def __mul__(self, other):
		if (self.column_count != other.row_count):
			print("Wrong matrix dimensions, cannot multiply", file = sys.stderr)
		else:
			M = Matrix(self.row_count, other.column_count)
			for row in self.rows:
				for column in other.columns:
					sum = 0
					for i in self.rows[row]:
						sum += self.read(int(row), int(i)) * other.read(int(i), int(column))
					M.set(int(row), int(column), sum)
			return M

m1 = Matrix(3, 4)
m1.set(2, 1, 5)
m1.set(2, 2, 1)
m1.print()

m2 = Matrix(3, 4)
m2.set(2, 2, 5)
m2.set(3, 4, 1)
m2.print()

M = m1 + m2
M.print()

m1 = Matrix(2, 1)
m1.set(1, 1, 1)
m1.set(2, 1, 5)
m1.print()

m2 = Matrix(1, 2)
m2.set(1, 1, 1)
m2.set(1, 2, 2)
m2.print()

M = m1 * m2
M.print()
M = m2 * m1
M.print()
