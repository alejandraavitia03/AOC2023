special_characters = "!@#$%^&*()-+?_=,<>/"
nums = ""
directions = [[0, 1], [0, -1], [1, 0], [-1, 0],
              [1, 1], [-1, 1], [1, -1], [-1, -1]]
dirs = [[0, 1], [0, -1]]
values = open('Dec3\engine-schematics.txt', 'r')
part_nums = values.readlines()
stripped_parts = [p.rstrip() for p in part_nums]
parts = [list(p) for p in stripped_parts]

row = len(parts)
col = len(parts[0])

symbol_locations = []
seen = []

# Get the locations of all the symbols
for r in range(row):
    seen.append([False, False, False, False, False,
                False, False, False, False, False])
    for c in range(col):
        if parts[r][c] in special_characters:
            symbol_locations.append([r, c])
#print(symbol_locations)


for loc in symbol_locations:
    currX = loc[0]
    currY = loc[1]
    print("For symbol: ", parts[currX][currY])
    for d in directions: #[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]
        x = currX + d[0]
        y = currY + d[1]

        if parts[x][y].isdigit():
            #Call a function that gets the number 
            # num_to_add = findNum(parts[x], y)
            seen[x][y] = True 

            print("a nummber!: ", parts[x][y], )
    print('\n')
# print(seen)
print('\n'.join(map(''.join, parts)))


def findNum(row, i) -> int:
    start_i = 0
    end_i = 0
    num = " "
    while start_i < y:
        if row[]
    for r in row:
        while end_i < len(row) and row[end_i].isdigit():
            end_i += 1
            num = num = row[end_i]

    return num
