#! /usr/bin/env python3

import random

basic="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
special = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

def password_gen(length=10, specials=3):
	list = [i for i in range(length)]
	password = [i for i in range(length)]
	random.shuffle(list)
	for i in range(0, specials):
		password[list.pop()] = random.choice(special)
	for i in list:
		password[i]= random.choice(basic)
	return password

print("".join(password_gen()))

