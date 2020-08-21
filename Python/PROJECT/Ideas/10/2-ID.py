#!/usr/bin/python
#NUMBER GUESSING

from random import *

min = randint(0, 50)
MAX = randint(50, 100)

Random_Number = 10

def Guessing_Number_Game():

    Random_Number = randint(min, MAX)
    print(Random_Number)

    print('range = [ '+str(min)+' | '+str(MAX)+' ]')
    Guessing_Number = int(input('Number: '))

    R = 0

    if Guessing_Number == Random_Number and R < 5:
        print('YOU WIN THE GAME!! ')
        print('CONGRATULATION')
        print('IF YOU WANT PLAY AGAIN PRESS [ 1 ]')
        Status = int(input(': '))
        if Status == 1:
            Guessing_Number_Game()
        else:
            print('BYE')

    elif Guessing_Number != Random_Number and R < 5:
        print('THE NUMBER IS WRONG')
        if Guessing_Number < Random_Number:
            print('YOUR NUMBER IS LESS THAN RANDOM NUMBER')
            R = R + 1
            print(R)
            Guessing_Number = int(input('Number: '))
        elif Guessing_Number > Random_Number:
            print('YOUR NUMBER IS GRATER THAN RANDOM NUMBER')
            R = R + 1
            print(R)
            Guessing_Number = int(input('Number: '))

    if R == 5:
        print('GAME OVER!!')
        print('IF YOU WANT PLAY AGAIN PRESS [ 1 ]')
        Status = int(input(': '))
        if Status == 1:
            Guessing_Number_Game()

        else:
            ('BYE!!')

Guessing_Number_Game()
