Riccardo_Curci = {
	"User": {
		"School": {
			"computer": "curci.riccardo",
		},
		"Mail": {
			"Gmail": "curci.richi@gmail.com",
			"Yahoo": "ric.cur@yahoo.com",
			"iCloud": "richi.curci@gmail.com",
		},
		"Debit_Card": {
			"Hype": "richi.curci@gmail.com",
		}, 
		"Site": {
			"Hack_The_Box": "curci.richi@gmail.com"
		}
	},

	"Password": {
		"School": {
			"computer": "studente",
		},
		"Mail": {
			"Gmail": "127cinque20051RiccardoCurci20051",
			"Yahoo": "27Cinque2005RiccardoCurci2005",
			"iCloud": "27Cinque2005RiccardoCurci2005",
		}, 
		"Debit_Card": {
			"Hype": "27Cinque2005Riccardo"
		}, 
		"Site": {
			"Hack_The_Box": "27Cinque2005RiccardoCurci2005",
		}
	}
}


def Secure():
	 
	Label_1 = input("Enter the category: ")
	Label_2 = input("Enter the name: ")
	print("")
	print("User: ",Riccardo_Curci["User"][Label_1][Label_2])
	print("")
	print("Password: ",Riccardo_Curci["Password"][Label_1][Label_2])

def Add():
	 
	Label_1 = input("Enter category: ")
	Label_2 = input("Enter the name: ")
	Label_3 = input("Enter the USER: ")
	Label_4 = input("Enter the PASSWORD: ")
	
	Riccardo_Curci ["User"][Label_1][Label_2] = Label_3
	Riccardo_Curci ["Password"][Label_1][Label_2] = Label_4
	
	print("User: ",Riccardo_Curci["User"][Label_1][Label_2])
	print("Password: ",Riccardo_Curci["Password"][Label_1][Label_2])
	
	

HomePage = """
Welcome to Secure this page can return your USER and PASSWORD of your acoounts. 
This service are ooffert by INLine company
	
	[ 0 ]Continuos
	[ 1 ]Exit
	
	[ 2 ]Add


"""
print(HomePage)
Label = input("$//: ")
if Label == "0": 
	Secure()
elif Label == "1": 
	print("Bye-Bye")
elif Label == "2": 
	Add()

