#!/usr/bin/python

#Converter of temperature from K to °C		(0/0)
def KTC():
	INLabel = input("Enter the temterature in K -->")
	Converter = float(INLabel)
	Logic = Converter - 273

	OULabel = Logic
	print("The temperature in °C is:")
	return OULabel


#Convert of temeperature from °C to K		(0/1)
def CTK():
	INLabel = input("Enter the temperature in °C -->")
	Converter = float(INLabel)
	Logic = Converter + 273,15

	OULabel = Logic
	print("The temperature in K is:")
	return OULabel


# m/m Concentration		(1/0)
def mm():
	INLabel_1 = input("Enter the mass of solute -->")
	Converter_1 = int(INLabel_1)

	INLabel_2 = input("Enter the mass of solvent -->")
	Converter_2 = int(INLabel_2)

	Logic = (Converter_1 / Converter_2) * 100
	return Logic

# m/V Concentration (1/1)
def mV():
	INLabel_1 = input("Enter the mass of solute -->")
	Converter_1 = int(INLabel_1)

	INLabel_2 = input("Enter the volume of solution -->")
	Converter_2 = int(INLabel_2)

	Logic = (Converter_1 / Converter_2) * 100
	return Logic

def VV():
	INLabel_1 = input("Enter the volume of solute -->")
	Converter_1 = int(INLabel_1)

	INLabel_2 = input("Enter the volume of solution -->")
	Converter_2 = int(INLabel_2)

	Logic = (Converter_1 / Converter_2) * 100
	return Logic
#HomePage
HomePage = """
Scienze

	[ 1 ] Temperature
	[ 2 ] Concentration

"""
TemperaturePage = """
Scienze/Temperature

 	[ 1 ] Kelvin to Celcius
 	[ 2 ] Celcius to Kelvin

"""
ConcentrationPage = """
Scienze/Concetration

	[ 1 ] m/m %
	[ 2 ] m/V %
	[ 3 ] V/V %

"""
print(HomePage)
Cursor = input("$//: ")
if Cursor == "1":
	print(TemperaturePage)
	Cursor = input("$/1//: ")
	if Cursor == "1":
		print(KTC())
	elif Cursor == "2":
		print(CTK())

elif Cursor == "2":
	print(ConcentrationPage)
	Cursor = input("$/2//: ")
	if Cursor == "1":
		print(mm())
	elif Cursor == "2":
		print(mV())
	elif Cursor == "3":
		print(VV())
