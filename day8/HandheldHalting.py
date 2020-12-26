#nop +0
#acc +1
#jmp +4


boot_code = []

#read data to list of list. First item in a list is int that shows how many times instruction has been visited

with open('day8.data','r') as f:
    data = f.read().splitlines()

    for item in data:
        boot_code.append([0, item.partition(' ')[0], int(item.partition(' ')[2])])

#part1

accumulator = 0
index = 0

while True:

    if boot_code[index][0] == 1:
        break
    
    if boot_code[index][1] == 'nop':
        boot_code[index][0] += 1
        index += 1
    
    if boot_code[index][1] == 'acc':
        accumulator += boot_code[index][2]
        boot_code[index][0] += 1
        index += 1

    if boot_code[index][1] == 'jmp':
        boot_code[index][0] += 1
        index += boot_code[index][2]

print('part1 accumulator:', accumulator)
assert(accumulator == 2014)
