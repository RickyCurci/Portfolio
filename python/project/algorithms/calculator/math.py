#!/usr/bin/python

import os

class Matematica:
	def __init__(self,Teoria,Esercizi_in_classe,Esercizi_a_casa):
		self.Teoria = Teoria
		self.Esercizi_in_classe = Esercizi_in_classe
		self.Esercizi_a_casa = Esercizi_a_casa
	def DataBase(self):
		return f"Argomenti:\n Teoria:   {self.Teoria}\n Esercizi in classe:   {self.Esercizi_in_classe}\n Esercizi a casa:   {self.Esercizi_a_casa}"

Insiemi = Matematica("TI1","EICI1","EACI1")
Monomi = Matematica("TM2","EICM2","EACM2")
Polinomi = Matematica("TP3","EICP3","EACP3")

ArgumentsList = [
	"insiemi",
	"monomi",
	"polinomi",
	"Insiemi",
	"Monomi",
	"Polinomi",
]

TotalArguments = [
	ArgumentsList[3],
	ArgumentsList[4],
	ArgumentsList[5]
	]
#Script UI
Homepage = """
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||  _   _   ____ _____  _____  _   _    ____ _____    _____  ____    |||
||| | \_/ | |____|  |   |___   | \_/ |  |____|  |   | |      |____|   |||
||| |     | |    |  |   |_____ |     |  |    |  |   | |_____ |    |   |||
|||                                                                   |||
||| In this shell you can see a position of math arguments in the     |||
||| database. Just enter the of the arguments when you will be asked  |||
|||                                                                   |||
||| Enter:                                                            |||
||| [ 1 ] to continue                                                 |||
||| [ 0 ] to exit                                                     |||
|||                                                                   |||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

"""
Secondpage = """
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||| Homepage/Secondpage                                               |||
|||                                                                   |||
||| Enter:                                                            |||
||| [ 2 ] to serch the arguments position in a database               |||
||| [ 1 ] to show the list of arguments                               |||
||| [ 0 ] to exit                                                     |||
|||                                                                   |||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

"""
Thirdpage = """
Homepage/Secondpage/Thirdpage
Enter the correct and complite name of the arguments:
"""
print(Homepage)
#Homepage Logic UI
HomepageSupport = ["0","1"]
HomePageLabel = input("Enter an parameter -->")
if HomePageLabel == HomepageSupport[1]:
	print(Secondpage)
else:
	print("Parameter are incorrect")
if HomePageLabel == HomepageSupport[0]:
	print("Good bye!!")
#Secondpage Logic UI
SecondpageSupport = ["0","1","2"]
SecondpageLabel = input("Enter an parameter -->")
if SecondpageLabel == SecondpageSupport[2]:
	print(Thirdpage)
if SecondpageLabel == SecondpageSupport[1]:
	print(TotalArguments)
if SecondpageLabel == SecondpageSupport[0]:
	print("Good bye!!")
#Thirdpage Logic UI
ThirdpageSupport = ["0"]
ThirdpageLabel = input("Enter the complite name -->")
if ThirdpageLabel == ArgumentsList[0]:
	print(Matematica.DataBase(Insiemi))
if ThirdpageLabel == ArgumentsList[1]:
	print(Matematica.DataBase(Monomi))
if ThirdpageLabel == ArgumentsList[2]:
	print(Matematica.DataBase(Polinomi))
if ThirdpageLabel == ArgumentsList[3]:
	print(Matematica.DataBase(Insiemi))
if ThirdpageLabel == ArgumentsList[4]:
	print(Matematica.DataBase(Monomi))
if ThirdpageLabel == ArgumentsList[5]:
	print(Matematica.DataBase(Polinomi))
elif ThirdpageLabel == ThirdpageSupport[0]:
	print("Good bye!!")
