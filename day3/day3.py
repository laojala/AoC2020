treemap = []

f=open("input.data","r")
for line in f:
    treemap.append(line.strip('\n'))

row_length = len(treemap[0])

x = 0
y = 0

trees = 0

while y < len(treemap) - len(treemap) % 2:
    x = x + 3
    y = y + 1
    
    if x >= row_length:
        x = x-row_length
    
    if treemap[y][x] == "#":
        trees = trees + 1

print(trees)





