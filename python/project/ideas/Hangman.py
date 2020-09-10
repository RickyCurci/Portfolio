#!/usr/bin/python3
from random import *

words = [ 'riccardo', 'aereodinamic', 'train', 'love', 'ferrari']
guessing_letter = []

base = [' +--+ ',   ' |  |   ', '    |   ', '    |   ', '    |   ', ' ======']
man =  [' O  |   ', '/|  |', '/|\ |', '/   |', '/ \ |']

life = list(range(0, len(man)))

words = words[randint(0, len(words))]
word = [words[int(i)] for i in range(0, len(words))]

for i in range(0, len(word)):
    guessing_letter.append('_')


def guessing():

    X = input("Guessing Word: ")

    for i in life:
      for letter in word:

        if letter == X:
            for i in range(-1, 3):

                position = word.index(letter)
                guessing_letter[position] = letter

                word[position] = '*'

                if letter not in word:
                    break

            printer()
            print(' ')
            print(guessing_letter)

            guessing_word = ''.join(str(i) for i in guessing_letter)
            if guessing_word == words:
                print('============================')
                print(' ')
                print('You win the match!')

                break

            guessing()

        elif letter != word:

            base[i + 2] = man[i]

            if i == 2 and base[3] == man[1]:
              base[3] = man[2]
              life.remove(i)

            elif i == 4 and base[4] == man[3]:
              base[4] = man[4]
              life.remove(i)

            else:
              life.remove(i)

            printer()
            print(guessing_letter)
            guessing()





def printer():
    for i in range(0,len(base)):
        print(base[i])


guessing()
