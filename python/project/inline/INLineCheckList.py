Name = """																	            INLineCheckList																				 """
One_Contents = [[""],[""], [""], [""], [0]] 
Two_Contents = [[""],[""], [""], [""], [0]] 
Theere_Contents = [[""],[""], [""], [""], [0]] 
Four_Contents = [[""],[""], [""], [""], [""], [0]]   
Five_Contents = [[""],[""], [""], [""], [""], [0]]   

class List: 
	def __init__(self,One,Two,Theere,Four,Five): 
		self.One = One
		self.Two = Two 
		self.Theere = Theere
		self.Four = Four
		self.Five = Five 
		
	def Page(self): 
		return f"\n1: {self.One} \n2: {self.Two} \n3: {self.Theere} \n4: {self.Four} \n5: {self.Five}"
		
CkecList = List(One_Contents,Two_Contents,Theere_Contents,Four_Contents,Five_Contents)
print(Name)
print(List.Page(CkecList))
