Days = ["Monday","Thuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
HomePage = """				       								            INLineCalendar 																 """


	
MondayItem_1 = [["Matematica"], ["Espressione sul quaderno"]]
MondayItem_2 = [["Religione"], ["Verifica"]]
MondayItem_3 = [[""], [""]]
MondayItem_4 = [[""], [""]]
MondayItem_5 = [[""], [""]]

ThuesdayItem_1 = [[""], [""]]
ThuesdayItem_2 = [[""], [""]]
ThuesdayItem_3 = [[""], [""]]
ThuesdayItem_4 = [[""], [""]]
ThuesdayItem_5 = [[""], [""]]

WednesdayItem_1 = [[""], [""]]
WednesdayItem_2 = [[""], [""]]
WednesdayItem_3 = [[""], [""]]
WednesdayItem_4 = [[""], [""]]
WednesdayItem_5 = [[""], [""]]

ThursdayItem_1 = [["Scienze"], ["Fare esercizzi sul quaderno"], ["Relazione si Laboratoro"]]
ThursdayItem_2 = [[""], [""]]
ThursdayItem_3 = [[""], [""]]
ThursdayItem_4 = [[""], [""]]
ThursdayItem_5 = [[""], [""]]

FridayItem_1 = [[""], [""]]
FridayItem_2 = [[""], [""]]
FridayItem_3 = [[""], [""]]
FridayItem_4 = [[""], [""]]
FridayItem_5 = [[""], [""]]

SaturdayItem_1 = [["Italiano"], ["Leggere libro per verifica"]]
SaturdayItem_2 = [[""], [""]]
SaturdayItem_3 = [[""], [""]]
SaturdayItem_4 = [[""], [""]]
SaturdayItem_5 = [[""], [""]]

SundayItem_1 = [[""], [""]]
SundayItem_2 = [[""], [""]]
SundayItem_3 = [[""], [""]]
SundayItem_4 = [[""], [""]]
SundayItem_5 = [[""], [""]]

class Calendar:  
    def __init__(self,Title,Item_1,Item_2,Item_3,Item_4,Item_5):
        self.Title  = Title 
        self.Item_1 = Item_1
        self.Item_2 = Item_2
        self.Item_3 = Item_3
        self.Item_4 = Item_4
        self.Item_5 = Item_5

    def Page(self): 
        return f"""\n {self.Title}\n{self.Item_1}\n{self.Item_2}\n{self.Item_3}\n{self.Item_4}\n{self.Item_5}\n """

class Monday(Calendar): 
	def __init__(self,Title,Item_1,Item_2,Item_3,Item_4,Item_5):
		super().__init__(Title,Item_1,Item_2,Item_3,Item_4,Item_5)
	def Page(self):
		return super().Page()

class Thuesday(Calendar): 
	def __init__(self,Title,Item_1,Item_2,Item_3,Item_4,Item_5):
		super().__init__(Title,Item_1,Item_2,Item_3,Item_4,Item_5)
	def Page(self):
		return super().Page()

class Wednesday(Calendar):
	def __init__(self,Title,Item_1,Item_2,Item_3,Item_4,Item_5):
		super().__init__(Title,Item_1,Item_2,Item_3,Item_4,Item_5)
	def Page(self):
		return super().Page()
		
class Thursday(Calendar): 
	def __init__(self,Title,Item_1,Item_2,Item_3,Item_4,Item_5): 
		super().__init__(Title,Item_1,Item_2,Item_3,Item_4,Item_5)
	def Page(self): 
		return  super().Page()
		
class Friday(Calendar): 
	def __init__(self,Title,Item_1,Item_2,Item_3,Item_4,Item_5): 
		super().__init__(Title,Item_1,Item_2,Item_3,Item_4,Item_5)
	def Page(self): 
		return super().Page() 
		
class Saturday(Calendar): 
	def __init__(self,Title,Item_1,Item_2,Item_3,Item_4,Item_5): 
		super().__init__(Title,Item_1,Item_2,Item_3,Item_4,Item_5)
	def Page(self): 
		return super().Page()	
		
class Sunday(Calendar): 
	def __init__(self,Title,Item_1,Item_2,Item_3,Item_4,Item_5): 
		super().__init__(Title,Item_1,Item_2,Item_3,Item_4,Item_5)
	def Page(self): 
		return super().Page()
	
Monday = Monday(Days[0],MondayItem_1,MondayItem_2,MondayItem_3,MondayItem_4,MondayItem_5)
Thuesday = Thuesday(Days[1],ThuesdayItem_1,ThuesdayItem_2,ThuesdayItem_3,ThuesdayItem_4,ThuesdayItem_5)
Wednesday = Wednesday(Days[2],WednesdayItem_1,WednesdayItem_2,WednesdayItem_3,WednesdayItem_4,WednesdayItem_5)
Thursday = Thursday(Days[3],ThursdayItem_1,ThursdayItem_2,ThursdayItem_3,ThursdayItem_4,ThursdayItem_5)
Friday = Friday(Days[4],FridayItem_1,FridayItem_2,FridayItem_3,FridayItem_4,FridayItem_5) 
Saturday = Saturday(Days[5],SaturdayItem_1,SaturdayItem_2,SaturdayItem_3,SaturdayItem_4,SaturdayItem_5)
Sunday = Sunday(Days[6],SundayItem_1,SundayItem_2,SundayItem_3,SundayItem_4,SundayItem_5)

def Printer(): 
	print(HomePage)
	print(Monday.Page())
	print(Thuesday.Page())
	print(Wednesday.Page())
	print(Thursday.Page())
	print(Friday.Page())
	print(Saturday.Page())
	print(Sunday.Page()) 
	
	
Printer()
