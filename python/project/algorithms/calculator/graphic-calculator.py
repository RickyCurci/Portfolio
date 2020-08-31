#!/usr/bin/python

def Calculator():

	Filter = """
	[ 0 ]+  [ 1 ]*  [ 2 ]-  [ 3 ]/
	"""
	print(Filter)
	Line = int(input("Operation: "))
	if Line == 0:
		First_INT = int(input(":"))
		Second_INT = int(input(":"))

		Result = First_INT + Second_INT

		print(Result)

	elif Line == 1:
		First_INT = int(input(":"))
		Second_INT = int(input(":"))

		Result = First_INT * Second_INT

		print(Result)


	elif Line == 2:
		First_INT = int(input(":"))
		Second_INT = int(input(":"))

		Result = First_INT - Second_INT

		print(Result)

	elif Line == 3:
		First_INT = int(input(":"))
		Second_INT = int(input(":"))

		Result = First_INT / Second_INT

		print(Result)

def Graphic():
	x = [0,1,3,-2,]
	y = []

	F = int(input("#//:"))
	for i in x:
		f = F*x[i]
		y.append(f)

	print(x,y)

Page = """
[ 0 ]Calculator
[ 1 ]Graphic
"""
print(Page)
Line = int(input("|:"))



if Line == 0:
	Calculator()
elif Line == 1:
	Graphic()
