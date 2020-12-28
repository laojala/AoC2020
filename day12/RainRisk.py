data = []

with open('day12.data','r') as f:
    lines = f.read().splitlines()
    for line in lines:
        action = line[0]
        value = int(line[1:])
        data.append([action, value])

degrees_to_letters = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W',
}

#first item is direction in degrees and second is coordinates
boat = [90,[0,0]]

for item in data:
    instruction = item[0]
    value = item[1]

    if instruction == 'F':
        instruction = degrees_to_letters[boat[0]]
    
    if instruction == 'N':
        boat[1][0] += value
        continue
    if instruction == 'S':
        boat[1][0] -= value
        continue
    if instruction == 'E':
        boat[1][1] += value
        continue
    if instruction == 'W':
        boat[1][1] -= value
        continue
    if instruction == 'R':
        boat[0] = (boat[0] + value) % 360
        continue
    if instruction == 'L':
        boat[0] = (boat[0] - value) % 360
        continue

part1 = abs(boat[1][0]) + abs(boat[1][1])
print('part1:', part1)
assert(part1 == 1441)