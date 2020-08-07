import time 
Mate = [
	["ITALIANO",[]],
	["FISICA",[]],
	["LATINO",[]],
	["ARTE",[]],
	["MATEMATICA",[]],
	["SCIENZE",[]],
	["STORIA",[]],
	["INGLESE",[]]
		
	
]
class School: 
	def __init__(self,Subject,Mate,Media): 
		self.Subject = Subject
		self.Mate = Mate
		self. Media = Media
	
	def Page(self): 
		f" {self.Subject}: {self.Mate} --> {self.Marks}"
		 

ITALIANO = School(Mate[0],Mate[0][1],"Work in progress")
FISICA = School(Mate[0],Mate[0][1],"Work in progress")
