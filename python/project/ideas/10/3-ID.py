#!/usr/bin/python
#DICE ROLLING [ 3 ]

from random import *

def Generate_Number():
    Random_Number = randint(0,6)
    print('NUMBER IS: '+str(Random_Number))
    
print(' ')
print('ROLL THE DICE [ 1 ]')
Status = int(input(': '))
if Status == 1:
    Generate_Number()
