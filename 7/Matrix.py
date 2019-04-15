#! /usr/bin/env python3

import copy
import sys

class Matrix:
	def __init__(self, rows, columns):
		self.row_count = rows
		self.column_count = columns
		self.rows = {"0": {"0":0}}
	def set(self, row, column, number):	# counted form 1
		if str(row) in self.rows:
			self.rows[str(row)][str(column)] = number
		else:
			c = {str(column) : number}
			self.rows[str(row)] = c

	def read(self, row, column):
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
			print("Cannot add different dimensions od matrices", file = sys.stderr)
		else:
			m = copy.deepcopy(self)
			for i in range(1, other.row_count+1):
				for j in range(1, other.column_count+1):
					m.set(i, j, self.read(i, j) + other.read(i, j))
			return m


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
