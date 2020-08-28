from random import * 
print("""

ENTER 
	
	[ 0 ]Player_1 vs CPU 
	[ 1 ]Player_1 vs Player_2
	
""")
Chooser = input("> ")

Status = False
Scene = [ 
    [[],[],[]],
    [[],[],[]],
    [[],[],[]]
]

def Printer(): 
	
	print(Scene[0])
	print(Scene[1])
	print(Scene[2])

def Player_1(): 
	
	Line = int(input("Line(1 to 3): "))-1
	Column = int(input("Column(1 to 3): "))-1
	
	if Scene[Line][Column] != 1: 
		
		Scene[Line][Column] = 0
		Printer()
		print(" ")
		
		
	else: 
		
		print(" ")
		print("POSITION IS ALREADY OCCUPED")
		print(" ")
		print(" ")
		Player_1()
	
def Player_2():
	
	if Chooser == 0: 
		
		def CPU(): 
			
			Line = randint(0,2)
			Column = randint(0,2)
			
			if Scene[Line][Column] != 0: 
				
				Scene[Line][Column] = 1
				Printer()
				print(" ")
				
			else: 
				
				print(" ")
				CPU()
				
		CPU()
		
	elif Chooser == 1: 
		
		def Player_2(): 
			
			Line = int(input("Line(1 to 3: ")) - 1 
			Column = int(input("Line(1 to 3: )")) - 1 
			
			if Scene[Line][Column] != 0: 
				
				Scene[Line][Column] = 1
				print(" ")
				
			else: 
				
				print(" ")	
				print("POSITION IS ALREADY OCCUPED")
				print(" ")
				print(" ")
				Player_2()
		
		Player_2()
				
for i in range(0,9): 
	if Scene[0][0] == 1 and Scene[0][1] == 1 and Scene[0][2] == 1:
		print("PLAYER 2 WIN THE GAME") 
		Status = True
		break
	elif Scene[1][0] == 1 and Scene[1][1] == 1 and Scene[1][2] == 1: 
		print("PLAYER 2 WIN THE GAME") 
		Status = True
		break
	elif Scene[2][0] == 1 and Scene[2][1] == 1 and Scene[2][2] == 1: 
		print("PLAYER 2 WIN THE GAME") 
		Status = True
		break
	elif Scene[0][0] == 1 and Scene[1][0] == 1 and Scene[2][0] == 1: 
		print("PLAYER 2 WIN THE GAME") 
		Status = True
		break
	elif Scene[0][0] == 1 and Scene[1][0] == 1 and Scene[2][0] == 1: 
		print("PLAYER 2 WIN THE GAME") 
		Status = True
		break
	elif Scene[0][0] == 1 and Scene[0][1] == 1 and Scene[0][2] == 1: 
		print("PLAYER 2 WIN THE GAME") 
		Status = True
		break
	elif Scene[1][0] == 1 and Scene[1][1] == 1 and Scene[1][2] == 1:
		print("PLAYER 2 WIN THE GAME") 
		Status = True
		break
	elif Scene[2][0] == 1 and Scene[2][1] == 1 and Scene[2][2] == 1:
		print("PLAYER 2 WIN THE GAME") 
		Status = True
		break
	elif Scene[0][0] == 1 and Scene[1][1] == 1 and Scene[2][2] == 1:
		print("PLAYER 2 WIN THE GAME") 
		Status = True
		break
	elif Scene[0][2] == 1 and Scene[1][1] == 1 and Scene[2][0] == 1:
		print("PLAYER 2 WIN THE GAME") 
		Status = True
		break
	
	elif Scene[0][0] == 0 and Scene[0][1] == 0 and Scene[0][2] == 0:
		print("PLAYER 1 WIN THE GAME") 
		Status = True
		break
	elif Scene[1][0] == 0 and Scene[1][1] == 0 and Scene[1][2] == 0: 
		print("PLAYER 1 WIN THE GAME") 
		Status = True
		break
	elif Scene[2][0] == 0 and Scene[2][1] == 0 and Scene[2][2] == 0:
		print("PLAYER 1 WIN THE GAME") 
		Status = True
		break
	elif Scene[0][0] == 0 and Scene[1][0] == 0 and Scene[2][0] == 0:
		print("PLAYER 1 WIN THE GAME") 
		Status = True
		break
	elif Scene[0][0] == 0 and Scene[1][0] == 0 and Scene[2][0] == 0: 
		print("PLAYER 1 WIN THE GAME") 
		Status = True
		break
	elif Scene[0][1] == 0 and Scene[0][1] == 0 and Scene[0][2] == 0: 
		print("PLAYER 1 WIN THE GAME") 
		Status = True
		break
	elif Scene[1][0] == 0 and Scene[1][1] == 0 and Scene[1][2] == 0:
		print("PLAYER 1 WIN THE GAME") 
		Status = True
		break
	elif Scene[2][0] == 0 and Scene[2][1] == 0 and Scene[2][2] == 0: 
		print("PLAYER 1 WIN THE GAME") 
		Status = True
		break
	elif Scene[0][0] == 0 and Scene[1][1] == 0 and Scene[2][2] == 0:
		print("PLAYER 1 WIN THE GAME") 
		Status = True
		break
	elif Scene[0][2] == 0 and Scene[1][1] == 0 and Scene[2][0] == 0:
		print("PLAYER 1 WiN THE GAME")
		Status = True
		break
		
	elif Status != True:

		Player_1()
		print(" ")
		Player_2()
	

