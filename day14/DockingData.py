import re

with open("day14.data", 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]

memory = {}
mask = ''
memory_slot = ''

for line in lines:
    value = ''
    k, v = line.split(" = ")
    if k == 'mask':
        mask = v
        continue
    else:
        memory_slot = int(re.search(r'\d+', k).group())
        value = "{0:b}".format(int(v))
        value = value.zfill(36)
    
    for index, char in enumerate(mask):
        if char == 'X':
            continue
        if char == '0':
            value = value[:index] + '0' + value[index + 1:]
        if char == '1':
            value = value[:index] + '1' + value[index + 1:]

    memory[memory_slot] = int(value, 2)

part1 = sum(memory.values())
print('part1:', part1)
assert(part1 == 9615006043476)
