#!/usr/bin/python3
from random import *
words = [ 'riccardo', 'aereodinamic', 'train', 'love', 'ferrari']
guessing_letter = []

base = ['+--+', '|  |   ', '   |   ', '   |   ', '   |   ', '======']
man = [ 'O  |   ', '  /|   ', '  /|\\ ']

words = words[randint(0, len(words))]
word = [words[int(i)] for i in range(0, len(words))]
print(word)


for i in range(0, len(word)):
    guessing_letter.append('_')


def guessing():

    X = input("Guessing Word: ")

    for letter in word:

        if letter == X:
            for i in range(-1, 3):
                position = word.index(letter)
                guessing_letter[position] = letter
                word.remove(letter)
                word[position] = '*'
                print(word[position])
                if letter not in word:
                    break

            printer()
            print(' ')
            print(guessing_letter)
            guessing()

            if guessing_letter == word:
                print(' ')
                print('============================')
                print(' ')
                print('you win the match')

def printer():
    for i in range(0,len(base)):
        print(base[i])


guessing()
