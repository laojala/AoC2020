data = []

with open('day12.data','r') as f:
    lines = f.read().splitlines()
    for line in lines:
        action = line[0]
        value = int(line[1:])
        data.append([action, value])

#first item is x and second is y
ship = [0,0]
waypoint = [10,1]


def rotate(waypoint, deg):
    # https://en.wikipedia.org/wiki/Rotation_matrix
    # solution from: #https://www.reddit.com/r/adventofcode/comments/kbj5me/2020_day_12_solutions/gfoewej/?utm_source=reddit&utm_medium=web2x&context=3
    rotations = { 
    "R90": [[0, 1], [-1, 0]],  "R180": [[-1, 0], [0, -1]], "R270": [[0,-1], [1,0]],
    "L90": [[0,-1], [1,0]], "L180": [[-1, 0], [0, -1]], "L270": [[0, 1], [-1, 0]]
    }

    r = rotations[deg]
    x, y = waypoint
    return [x*r[0][0] + y*r[0][1], x*r[1][0] + y*r[1][1]]


for item in data:
    instruction = item[0]
    value = item[1]

    if instruction == 'F':
        x = waypoint[0] * value
        y = waypoint[1] * value

        ship[0] += x
        ship[1] += y

    if instruction == 'N':
        waypoint[1] += value

    if instruction == 'S':
        waypoint[1] -= value

    if instruction == 'E':
        waypoint[0] += value

    if instruction == 'W':
        waypoint[0] -= value


    if instruction in ('L', 'R'):
        waypoint = rotate(waypoint, item[0]+str(item[1]))

part2 = abs(ship[0]) + abs(ship[1])
print('part2:', part2)
assert(part2 == 61616)

