treemap = []

f=open("input.data","r")
for line in f:
    treemap.append(line.strip('\n'))

row_length = len(treemap[0])

steps = ((1,1),(3,1),(5,1),(7,1),(1,2))

result = 1

for step in steps:

    x = 0
    y = 0

    trees = 0

    while y < len(treemap) - len(treemap) % 2:
        x = x + step[0]
        y = y + step[1]
        
        if x >= row_length:
            x = x-row_length
        
        if treemap[y][x] == "#":
            trees = trees + 1

    print(trees)

    result = result * trees


print(result)

