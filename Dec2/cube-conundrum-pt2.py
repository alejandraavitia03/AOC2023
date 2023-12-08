from collections import namedtuple
import re

sum = 0


values = open('Dec2\puzzle-input.txt', 'r')
games = values.readlines()

for game in games:

    # To store which ID we have and what we are adding
    i = re.search(r'\d+', game).group()
    print("game: ", i)
    # This is the index of the :
    c = game.rfind(':')
    # This is the draws for that game
    temp = game[c+1:]
    draws = temp.split(';')
    draws[-1] = draws[-1].replace('\n', '')
    print("Draws for game " + i + ": ", draws)
    y = 0
    maxG = 1
    maxR = 1
    maxB = 1
    l = 1
    greenSeen = 0
    redSeen = 0
    blueSeen = 0
    for draw in draws:
        x = draw.split(',')
        print("Draw #", str(l), ": ", x)

        for d in x:

            if 'green' in d:
                greenSeen = 1
                tempgreen = re.findall(r'\d+', d)
                if int(tempgreen[0]) > maxG:
                    maxG = int(tempgreen[0])
                    print('Found a new green max')

            elif 'blue' in d:
                blueSeen = 1
                tempblue = re.findall(r'\d+', d)
                if int(tempblue[0]) > maxB:
                    maxB = int(tempblue[0])
                    print('Found a new blue max')

            elif 'red' in d:
                redSeen = 1
                tempred = re.findall(r'\d+', d)

                if int(tempred[0]) > maxR:
                    maxR = int(tempred[0])
                    print('Found a new red max')

    print("At the end of game #", i, " the red max: ", str(maxR),
          ", the blue max: ", str(maxB), ",and the green max: ", maxG)
    y = int(maxR) * int(maxB) * int(maxG)
    sum += y
    print("Sum: ", sum, '\n')
