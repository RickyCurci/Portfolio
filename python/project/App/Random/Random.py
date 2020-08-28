import ui
from random import *

def TextField_Action(text): 
	#Limit = text
	pass
	
	
def Number_Random(self): 
	Limit = int(textfield.text)
	Output = randint(0,Limit)
	label.text = str(Output)
	
v = ui.load_view('Random.pyui')


textfield = v['Limit']
label = v['Result']
button = v['Generate']


textfield.action = TextField_Action 
button.action = Number_Random

v.present('sheet')
