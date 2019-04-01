#! /usr/bin/env python3

import sys

def palindrome_test(pal):
	for i in range(0, len(pal)//2):
		if pal[i]!=pal[len(pal)-1-i]:
			return False
	return True

pal = sys.argv[1]
print(palindrome_test(pal))
