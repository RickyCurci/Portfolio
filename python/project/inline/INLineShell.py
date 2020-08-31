First_FolderDIRECTORY = ["CODING"]
First_FolderFILE = ["Script.py","Text.txt"]
Second_FolderDIRECTORY = ["Python","Javascript","Php","Html","Css"]
Second_FolderFILE = [""]

class Folder: 
	def __init__(self,Name,Directory): 
		self.Name = Name 
		self.Directory = Directory
	def Shell(self):
		return f"{self.Name} \nDirectory:\n {self.Directory}\n"		
		
class Riccardo(Folder): 
	def __init__(self,Name,Directory,File): 
		super().__init__(Name,Directory)
		self.File = File
	def Shell(self):
		Shell = f"File:\n {self.File}"
		return super().Shell() + Shell 
class Coding(Folder): 
	def __init__(self,Name,Directory,File):
		super().__init__(Name,Directory)
		self.File = File 
		
	def Shell(self): 
		Shell = f"File \n {self.File}"
		return super().Shell() + Shell 
class Python(Folder): 
	def __init__(self,Name,Directory,File):
		super().__init__(Name,Directory)
		self.File = File
	def Shell(self):
		Shell = f"File:\n {self.File}" 
		return super().Shell() + Shell
		
First_Folder = Riccardo("Riccardo",First_FolderDIRECTORY,First_FolderFILE)
Second_Folder = Coding("Coding",Second_FolderDIRECTORY,Second_FolderFILE)
	
print(Riccardo.Shell(Second_Folder))

