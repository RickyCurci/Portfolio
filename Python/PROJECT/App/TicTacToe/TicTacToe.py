import ui

v = ui.load_view("TicTacToe.pyui")

one = v["1"]
two = v["2"]
three = v["3"]
four = v["4"]
five = v["5"]
six = v["6"]
seven = v["7"]
eight = v["8"]
nine = v["9"]

def ADD(): 
	one.title = "X"

def Player_1(): 
	one.action = ADD()
if one.title != "O": 
	Player_1()
	
	
v.present('sheet')
