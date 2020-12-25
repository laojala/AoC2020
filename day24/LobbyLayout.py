tiles = []

with open('24_input.data','r') as f:
    data = f.read().splitlines()

    for line in data:
        row  = []
        while (len(line) != 0):
            if line[0] == 'n' or line[0] == 's':
                row.append(line[0:2])
                line = line[2:]
            else:
                row.append(line[0:1])
                line = line[1:]
        tiles.append(row)

for row in tiles:
    print(row)
