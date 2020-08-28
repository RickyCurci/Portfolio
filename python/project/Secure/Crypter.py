#Crypter Function 
def AlphabetCrypter(): 
	#Title Part 
	Title = "Alphabet Crypter"
	print(Title)
	
	#Input Part
	Rules = "Enter a word with MAX 5 CHAR (Tiny char)"
	First = input("1: ")
	Second = input("2: ")
	Third = input("3: ")
	Fourth = input("4: ")
	Fifth = input("5: ")
	
	Words = [First,Second,Third,Fourth,Fifth]
	A = "a"
	B = "b"
	C = "c"
	D = "d"
	E = "e"
	F = "f"
	G = "g"
	H = "h"
	I = "i"
	L = "l"
	M = "m"
	N = "n"
	O = "o"
	P = "p"
	Q = "q"
	R = "r"
	S = "s"
	T = "t"
	U = "u"
	V = "v"
	Z = "z"
	K = "k"
	W = "w"
	Y = "y"
	X = "x"
	J = "j"
	for A in Words: 
		print(0) 
	for B in Words:
		print(1)
		
		
def ValueCrypter():	
	#Title Part 
	Title = "Value Crypter"
	print(Title)
	
	#Input Part
	Value = input("Enter the value: ")
	Key = input("Enter the traslaction key: ")
	
	#Crypter Part  
	CValue = int(Value)
	CKey = int(Key)
	
	#Logic Part
	Converter = CValue * CKey 
	Output = Converter	
	
	print(Output, CKey * 2)
	
def ValueDecrypter(): 
	#Title Part
	Title = "Decrypter"
	print(Title)
	
	#Input Part 
	Value = input("Enter the Crypted value: ")
	Key = input("Enter the key: ")
	
	#Decrypter Part
	CValue = int(Value)
	Ckey = int(Key)
	
	#Logic Part 
	Converter = CValue / Ckey
	Output = Converter
	print(Output)
	
def Alphabet():
	Alphabet = """
A: 0   O: 12
B: 1   P: 13 
C: 4   Q: 16
D: 5   R: 17
E: 2   S: 14
F: 3   T: 15
G: 6   U: 18
H: 7   V: 19
I: 10  Z: 20 
L: 11
M: 8
N: 9  
	"""
	print(Alphabet)

def Interface(): 
	Homepage = """
Pignus 

	[ 1 ] Crypter
	[ 2 ] Decrypter
	
	"""
	CrypterPage = """
Crypter 
	
	[ 1 ] AlphabetCrypter
	[ 2 ] ValueCrypter 
	
	"""
	DecrypterPage = """
Decrypter	
	
	[ 1 ] AlphabetDecrypter
	[ 2 ] ValueDecrypter
	"""
	print(Homepage)
	HomeLine = input("Enter: ")
	if HomeLine == "1": 
		print(CrypterPage)
		CrypterLine = input("Enter: ")
		if CrypterLine == "1": 
			print("Working Progress!!")
		if CrypterLine == "2":
			print(ValueCrypter())
		
	if HomeLine == "2": 
		print(DecrypterPage)
		DecrypterLine = input("Enter: ")
		if DecrypterLine == "1": 
			print("Working Progress!!")
		if DecrypterLine == "2": 
			print(ValueDecrypter())
		
#Password Part 	
Password = "3"
PasswordLabel = input("Password: ")


#Password Verify Part 
if PasswordLabel == Password: 
	print(Interface())
if not PasswordLabel == Password: 
	PasswordLabel = input("Password: ")	
	if PasswordLabel == Password: 
		print(Interface())
	if not PasswordLabel == Password: 
		PasswordLabel = input("Password: ")
		if PasswordLabel == Password: 
			print(Interface())
		if not PasswordLabel == Password: 
			print("Sorry, you have exahust the tentatives... REBOOT")
			
