#! /usr/bin/env python3

tuples = [(i,) for i in range(10)]

tuples2 = map(lambda i: (i,), range(10))


l=[]
for i in range(1, 11):
	for j in range(1, 11):
		l.append((i,j,i*j))
