n=10


a=1
b=1
def next():
	c=a+b
	a=b
	b=c
def fib(n):
	if n==0:
		return a
	for i in range(n):
		next()
	return a

fib(n)
