Ports = [
	["ssh", "Open"],
	["Ftp", "Close"],
	["Http", "Close"],
	["Kerberos", "Open"],
	]
Ip = "10.12.254.1"	
class Server: 
	def __init__(self,Name,Os,User,Password,Ports,Ip): 
		self.Name = Name
		self.Os = Os 
		self.Password = Password
		self.User = User
		self.Ports = Ports
		self.Ip = Ip 
		
	def Shell(self): 
		return f" Name:{self.Name} Os: {self.Os} \n User: {self.User} Password: {self.Password} \n	{self.Ports} \n \n {self.Ip}"
		
Server = Server("24-45-67 Server","Ubuntu-Server","Admin","Root",Ports,Ip)
ServerPage = """Server 24-45-67"""

def ServerPrinter(): 
	print(Server.Shell())
	File = "http://127.0.0.1:5000/"
	return File 
	
class Computer(): 
	def __init__(self,Name,Os,User,Password,Ports,Ip):
		self.Name = Name 
		self.Os = Os 
		self.User = User 
		self.Password = Password
		self.Ports = Ports
		self.Ip = Ip 
		
	def Shell(self):
		return f"Name:{self.Name} Os: {self.Os} \nUser: {self.User} Password: {self.Password} \n{self.Ports} \n \nIp: {self.Ip}"

Computer = Computer("Dell XPS 13","Ubuntu/MacOS", "Riccardo", "27Cinque2005RiccardoCurci2005", "Port: //","192.168.1,345")
ComputerPage = """Dell XPS 13"""
print(ComputerPage)


def Exploit():
	pass
def sshLogin(): 
	ServerSshPassword = "Root"
	SSHLine = input("Password: ")	
	if SSHLine == ServerSshPassword:
		return ServerPrinter()	

def ComputerShell():
	Commmands = [ "ssh", "exit", "help"]
	Line = input("$//: ")
	if Line == Commmands[2]:
		return Commmands
		Line = input("$//: ")
		if Line == Commmands[0]: 
			return sshLogin()  
		elif Line == Commmands[1]:
			return "[Process Complete]"
	elif Line == Commmands[0]:
		return sshLogin()
	elif Line == Commmands[1]:
		return "[Process Complete]"

def ComputerPrinter():
	print(Computer.Shell())
	print("")
	print(ComputerShell())
	
		
		
ComputerPassword = "3"
ComputerPasswordLabel = input("Password: ")
if ComputerPasswordLabel == ComputerPassword:
	print(ComputerPrinter())


#Shell ((SSh di accesso al server)e la password Kerberos)per. il computer non server 
