#! /usr/bin/env python3

class Rectangle:
	def __init__(self, x, y):
		self.set_size(x, y)
	def set_size(self, x, y):
		self.a, self.b = x, y
	def get_area(self):
		return self.a * self.b


r = Rectangle(4, 5)
print(r.get_area())
r.set_size(2, 6)
print(r.get_area())
