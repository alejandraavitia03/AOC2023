from collections import namedtuple
import re

sum = 0
redMAX = 12
greenMAX = 13
blueMAX = 14

validG = False
validR = False
validB = False

game = namedtuple('GameID', ['red', 'green', 'blue'])

values = open('Dec2\puzzle-input.txt', 'r')
games = values.readlines()

for g in games:
    validD = 0
    # To store which ID we have
    i = re.search(r'\d+', g).group()
    print("game: ", i)
    # This is the index of the :
    c = g.rfind(':')
    # This is the draws for that game
    temp = g[c+1:]
    print("Draws: ", temp)
    draws = temp.split(';')
    draws[-1] = draws[-1].replace('\n', '')
    print("Draws as a list: ", draws)

    validG = False
    validR = False
    validB = False

    for d in draws:
        x = d.split(',')
        print("Each draw as a list: ", x)
        green = 0
        red = 0
        blue = 0
        for play in x:
            if 'green' in play:
                green = 1
                tempgreen = re.findall(r'\d+', play)
                if int(tempgreen[0]) <= greenMAX:
                    validG = True

                    print(' in green true')
                else:
                    validG = False

            # else:
            #     validG = True
            elif 'blue' in play:
                blue = 1
                tempblue = re.findall(r'\d+', play)
                if int(tempblue[0]) <= blueMAX:
                    validB = True
                    print(' in blue true')
                else:
                    validB = False

            # else:
            #     validB = True

            elif 'red' in play:
                red = 1
                tempred = re.findall(r'\d+', play)

                if int(tempred[0]) <= 12:
                    validR = True
                    print(' in red true')
                else:
                    validR = False

            # else:
            #     validR = True
        print(red, blue, green)
        if red == 0:
            validR = True
        elif blue == 0:
            validB = True
        elif green == 0:
            validG = True

        if validR and validB and validG:
            validD += 1
            print(' draw was true')
    print(str(validD))
    if validD == len(draws):
        print("Adding: " + i)
        sum += int(i)
        print('game was true')
    print(sum, '\n')
