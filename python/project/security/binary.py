
def cls(): 
	print('\n'*100)
	
def Binary():
	def Converter():
		print("Enter the DECIMAL number to conveter this in a BINARY number")
		Number = int(input("$/0//:"))
		X = Number
		Binary = []
		while X > 0:
			if X % 2 != 0: 
				Binary.append(1)
			else: 
				Binary.append(0)
			X = X//2

		Binary.reverse()
		Binary = ''.join(str(i) for i in Binary)
		print("BINARY NUMBER IS:", int(Binary))
	
	def Return():
		SecondPage = """

	[ 0 ]Converter
	[ 1 ]Exit

		"""
		print(SecondPage)
		Label = int(input("$/0//: "))
		if Label == 0: 
			cls()
			Converter()
			Return()
		elif Label == 1: 
			cls()
			return "Bye"
	

	HomePage = """ 
BINARY

	[ 0 ]Converter
	[ 1 ]Exit
	
	"""
	print(HomePage)

	Label = input("$//:")
	if Label == 0:
		cls()
		Converter()
		Return()
	elif Label == "1": 
		cls()
		print("Bye")
		
def Decimal():
	def Converter():
		print("Enter BINARY number to converter this in a DECIMAL number")	
		Number = str(input("$/0//: "))
		X = Number

		X = [X[int(i)] for i in range(0, len(X))] 
		
		denary = 0  
		
		for digit in X: 
			denary = denary * 2 + int(digit)  
			
			
		Number = denary
		print("DECIMAL NUMBER is: ", int(Number))  
	def Return():
		SecondPage = """

	[ 0 ]Converter
	[ 1 ]Exit

		"""
		print(SecondPage)
		Label = int(input("$/0//: "))
		if Label == 0: 
			cls()
			Converter()
			Return()
		elif Label == 1: 
			cls()
			return "Bye"
		
	Converter()
	Return()
LunchPage = """
SECURE 
	
	[ 0 ]Decimal to Binary
	[ 1 ]Binary to Decinal
	[ 2 ]Exit
 
"""
print(LunchPage)
Label = int(input("$//:"))
if Label == 0:
	cls()
	Binary()
elif Label == 1:
	cls()
	Decimal() 
elif Label == 2:
	cls()
	print("Bye")
