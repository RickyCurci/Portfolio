#!/usr/bin/python
#NUMBER GUESSING [ 2 ]

from random import *

min = randint(0, 50)
MAX = randint(50, 100)

def Guessing_Number_Game():

    Random_Number = randint(min, MAX)

    print('range = [ '+str(min)+' | '+str(MAX)+' ]')
    def Round():

        Guessing_Number = int(input('Number: '))
        if Guessing_Number == Random_Number:
            print('YOU WIN THE GAME!! ')
            print('CONGRATULATION')
            print('IF YOU WANT PLAY AGAIN PRESS [ 1 ]')
            print('OR TO EXIT PRESS [ 0 ]')
            Status = int(input(': '))
            if Status == 1:
                Guessing_Number_Game()
            elif Status == 0:
                print('BYE')

        elif Guessing_Number != Random_Number:
            print('THE NUMBER IS WRONG')
            if Guessing_Number < Random_Number:
                print('YOUR NUMBER IS LESS THAN RANDOM NUMBER')

                Round()
            elif Guessing_Number > Random_Number:
                print('YOUR NUMBER IS GRATER THAN RANDOM NUMBER')

                Round()


    Round()

Guessing_Number_Game()
