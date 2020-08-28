def SECURE():
#Script UI
	HomePage = """
	
	//////////////////////MENU//////////////////////
	// Enter:                                     //
	// 1)Computer                                 //
	// 2)iCloud                                   //
	// 3)Gmail                                    //
	// 4)Yahoo                                    //
	// 5)Hype                    for add enter: + //
	////////////////////////////////////////////////
	
	"""
	print(HomePage)
#DataBase UI
	def Computer():
		ComputerUser = "curci.riccardo"
		ComputerPassword = "Studente"
		print("User: "+ComputerUser)
		print("Password: "+ComputerPassword)
	
	def iCloud():
		iCloudUser = "richi.curci@gmail.com"
		iCloudPassword = "27Cinque2005"
		print("User: "+iCloudUser)
		print("Password: "+iCloudPassword)
	
	def Gmail():
		GmailUser = "curci.richi@gmail.com"
		GmailPassword = "27cinque2005Riccardo"
		print("User"+GmailUser)
		print("Password: "+GmailPassword)
	
	def Yahoo(): 
		YahooUser = "ric.cur@yahoo.com"
		YahooPassword = "27Cinque2005"
		print("User: "+YahooUser)
		print("Password: "+YahooPassword)
	def Hype():
		HypeUser = "richi.curci@gmail.com" 
		HypePassword = "27Cinque2005"
		print("User: "+HypeUser)
		print("Password: "+HypePassword)
	def Add(): 
		AddParameterName = input("Inserisci il nome: ")
		AddParameterUser = input("Inserisci l'user: ")
		AddParameterPassword = input("Enter the Password:")
		print(AddParameterName)
		print(AddParameterUser)
		print(AddParameterPassword)

#Logic UI
	UserChoose = [
			"Computer","iCloud","Gmail","Yahoo","Hype","+"
			]
	HomeLabel = input("Inserisci un parametro: ")
	if HomeLabel == UserChoose[0]:
		Computer()
	elif HomeLabel == UserChoose[1]:
		iCloud()
	elif HomeLabel == UserChoose[2]:
		Gmail()
	elif HomeLabel == UserChoose[3]:
		Yahoo()
	elif HomeLabel == UserChoose[4]:
		Hype()
	elif HomeLabel == UserChoose[5]:
		Add()
Password = "27Cinque2005"
PasswordLabel = input("Inserisci la Password: ")
PasswordLabel1 = input("Inserisci la Password: ")
if PasswordLabel == Password:
	SECURE()
else:
	print("Password errata, Reinseriscila.   "+PasswordLabel1)
	if PasswordLabel1 == Password:
		SECURE()

