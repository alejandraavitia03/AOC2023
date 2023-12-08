from collections import namedtuple
import re

sum = 0
redMAX = 12
greenMAX = 13
blueMAX = 14

validG = False
validR = False
validB = False


values = open('Dec2\puzzle-input.txt', 'r')
games = values.readlines()

for g in games:
    # IF all the draws are valid then at the end of this loop validGame == how many draws there were
    validD = 0
    # To store which ID we have and what we are adding
    i = re.search(r'\d+', g).group()
    print("game: ", i)
    # This is the index of the :
    c = g.rfind(':')
    # This is the draws for that game
    temp = g[c+1:]
    draws = temp.split(';')
    draws[-1] = draws[-1].replace('\n', '')
    print("Draws for game " + i + ": ", draws)

    validG = False
    validR = False
    validB = False
    l = 1
    greenSeen = 0
    redSeen = 0
    blueSeen = 0
    for d in draws:

        # every draw split by color as one list
        x = d.split(',')
        print("Draw #", str(l), ": ", x)

        greenSeen = 0
        redSeen = 0
        blueSeen = 0

        for play in x:

            if 'green' in play:
                greenSeen = 1
                tempgreen = re.findall(r'\d+', play)
                if int(tempgreen[0]) <= greenMAX:
                    validG = True
                    print(' in green true')
                else:
                    validG = False
            elif 'blue' in play:
                blueSeen = 1
                tempblue = re.findall(r'\d+', play)
                if int(tempblue[0]) <= blueMAX:
                    validB = True
                    print(' in blue true')
                else:
                    validB = False
            elif 'red' in play:
                redSeen = 1
                tempred = re.findall(r'\d+', play)

                if int(tempred[0]) <= 12:
                    validR = True
                    print(' in red true')
                else:
                    validR = False
        # print(greenSeen)
        if redSeen == 0:
            validR = True
        if blueSeen == 0:
            validB = True
        if greenSeen == 0:
            validG = True

        if validR and validB and validG:
            validD += 1
            print(' draw was true')
        # print(validB, validG, validR)
        l += 1

    print(str(validD) + " out of " + str(len(draws)))
    if validD == len(draws):
        print("Adding: " + i)
        sum += int(i)
        print('game was true')
    print("Sum: ", sum, '\n')
