import ui
v = ui.load_view('Secure.pyui')

Riccardo_Curci = {
	"User": {
		
			"Computer": "curci.riccardo",

			"Gmail": "curci.richi@gmail.com",
			"Yahoo": "ric.cur@yahoo.com",
			"iCloud": "richi.curci@gmail.com",
			
			"Hype": "richi.curci@gmail.com",
			
			"Hack_The_Box": "curci.richi@gmail.com"
	},

	"Password": {

			"Computer": "studente",

			"Gmail": "127cinque20051RiccardoCurci20051",
			"Yahoo": "27Cinque2005RiccardoCurci2005",
			"iCloud": "27Cinque2005RiccardoCurci2005",
			
			"Hype": "27Cinque2005Riccardo",

			"Hack_The_Box": "27Cinque2005RiccardoCurci2005",
	}
}

def TextField_Action(text): 
	Site = text
	
def Search(self): 
	Site = textfield.text 
	UserLabel.text = Riccardo_Curci["User"][Site]
	PasswordLabel.text = Riccardo_Curci["Password"][Site]
	

textfield = v['Site']
button = v['Search']
UserLabel = v['User']
PasswordLabel = v['Password']

textfield.action = TextField_Action
button.action = Search


v.present('sheet')



