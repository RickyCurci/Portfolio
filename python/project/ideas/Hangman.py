#!:/usr/bin/python
from random import *
words = [ 'riccardo', 'aereodinamic', 'train', 'love', 'ferrari']
support = ['+--+', '|  |   ', '   |   ', '   |   ', '   |   ', '======']
man = [ 'O  |   ', '  /|   ', '  /|\\ ']

def printer():
    
    word =  words[randint(-1, len(words))].split()
    X = input("Guessing Word: ")
    
    for i in range(0,(len(man) + 2): 
        for letter in word: 
            if letter == X: 
                print('OK')
            
            elif letter != X:  
                support[i] = man[i]
    
    for i in range(0,len(support)):
        print(support[i])
        
        
printer()
   