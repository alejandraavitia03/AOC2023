values = open('calibration-values.txt','r')
lines = values.readlines()
sum = 0

for line in lines:
    if line[0].isdigit():
        first = line[0]
        print(first)
    
