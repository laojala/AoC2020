import os
from math import ceil

data = []

file_path=(os.path.dirname(__file__)) + 'day5.data'
with open(file_path,'r') as f:
    data = f.read().splitlines()


def calculateSpot(item, max_row, up, low):
    min_row = 0
    for char in item:
        if char == up:
            max_row = ((min_row + max_row) // 2) - 1
        elif char == low:
            min_row = ceil((min_row + max_row + 1)/2)
    return int(min_row)


id_list = []

for item in data:
    row = calculateSpot(item[0:7], 127, 'F', 'B')
    column =  calculateSpot(item[7:10], 7, 'L', 'R')
    seat_id = row * 8 + column
    id_list.append(int(seat_id))

#part 1
assert(max(id_list) == 955)
print('part1:', max(id_list))

#part 2
id_list.sort()
index = 0
part2_result = None

while index < len(id_list):
    if id_list[index] + 1 not in id_list:
        part2_result = id_list[index] + 1
        break
    index = index + 1

assert(part2_result == 569)
print('part2', part2_result)
