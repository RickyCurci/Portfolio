from random import * 
BatteryLevel = randint(0,100) 


airpods = randint(0,1)
airpodsID = "iPhone di RICCARDINO"
if airpods == 0:
	airpods = True 
elif airpods == 1:
	airpods = False


phone = randint(0,5)
phoneDistance = randint(0,5)
phoneID = "iPhone di RICCARDINO"

class Airpods:

	def Press(time):
		if time == 5 and airpods == True:
			Light = "white"
			return Light
			
		elif time == 1: 
			if BatteryLevel <= 50: 
				Light = "red"
			else: 
				Light = "green"
			return Light
		else:
			return "ERROR"
	
	def Connection():
		if phoneDistance <= 5 and phone == True and phoneID == airpodsID:
			connection = True, phoneID 
			return connection
		else: 
			return "ERROR"
			 
led = Airpods.Press(1)
connection = Airpods.Connection()
if connection == "ERROR":
	print("STATUS (",airpods,")","LED (",led,")","CONNECTION (",connection,")")
else:
	print("STATUS (",airpods,")","LED (",led,")","CONNECTION",connection,"")
# MODIFICARE IL PROTOCOLLO IPHONE DI CONNESSIONE 
