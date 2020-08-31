#!/usr/bin/python

Limit = 101

Number = []

Y = 1
for i in range(0, Limit):

	for i in range(0, Limit):

		if (i % Y) != 0:
			Number.append(i)

		else:
			pass


	Y = Y + 1
print(Number)
