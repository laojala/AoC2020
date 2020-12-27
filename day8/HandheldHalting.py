boot_code = []

#read data to list of list. First item in a list is int that shows how many times instruction has been visited

with open('day8.data','r') as f:
    data = f.read().splitlines()

    for item in data:
        boot_code.append([0, item.partition(' ')[0], int(item.partition(' ')[2])])

#part1

accumulator = 0
index = 0
boot_part1 = boot_code[:]

while True:

    if boot_part1[index][0] == 1:
        break
    
    if boot_part1[index][1] == 'nop':
        boot_part1[index][0] += 1
        index += 1
    
    if boot_part1[index][1] == 'acc':
        accumulator += boot_part1[index][2]
        boot_part1[index][0] += 1
        index += 1

    if boot_part1[index][1] == 'jmp':
        boot_part1[index][0] += 1
        index += boot_part1[index][2]

print('part1 accumulator:', accumulator)
#assert(accumulator == 2014)

#part2

def resetCode(code):

    newCode = []

    for item in code:
        if item[0] == 1:
            item[0] = 0
        if item[0] == 100:
            item[0] = 99
        newCode.append(item)
    
    return newCode


lenght = len(boot_code)
solved = False
accumulator = 0

while not solved:

    if solved:
        break

    index = 0
    accumulator = 0
    operation_changed = False #one operation changed on a round
    boot_code = resetCode(boot_code)

    while True:

        if(index == lenght):
            solved = True
            break

        visited = boot_code[index][0]
        operation = boot_code[index][1]
        argument = boot_code[index][2]

        if(visited == 1 or visited == 100):
            operation_changed = False
            break

        if operation == 'acc':
            accumulator += argument
            boot_code[index][0] += 1
            index += 1

        if operation == 'nop':
            #if not visited and not changed for this round, change operation:
            if visited == 0 and not operation_changed:
                boot_code[index][0] = 99
                operation_changed = True
                index += argument  #do jmp
            #otherwise do nop
            else:
                boot_code[index][0] += 1
                index += 1
        
        if operation == 'jmp':
            #if not visited and not changed in this round, change operation:
            if visited == 0 and not operation_changed:
                boot_code[index][0] = 99
                operation_changed = True
                index += 1  #do nop
            #otherwise do jmp
            else:
                boot_code[index][0] += 1
                index += argument

print('part2 accumulator:', accumulator)
assert(accumulator == 2251)
