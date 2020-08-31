from random import *
Letter = "ABCDEFGHIKLMNOPQRSTVXYZabcdefghiklmnopqrstuvxyz123456789#@"
Char =  [Letter[int(i)] for i in range(0, len(Letter))]

Limit = int(input("Enter the LIMIT(1 to 57): "))

def Generator():
	Password = []
	for i in range(0,57):
		Range = randint(0,55)
		Element = Char[Range + 2]
		Password.append(Element)
		
	Password.reverse()
	Password = Password[0: Limit]
	Password = "".join(str(i) for i in Password)
	print("YOUR PASSWORD IS: ",Password)
	
Generator()
