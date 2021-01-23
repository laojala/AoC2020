from time import time

#idea: dictionary where key is spoken value and value is turn it was last spoken.

def elfGame(rounds):
    starting = [6,3,15,13,1,0]
    turns = {}
    last_spoken = None

    for i in range(rounds):

        if starting:
            spoken = starting.pop(0)
            turns[spoken] = i
            last_spoken = spoken
            continue

        previous_turn = i-1

        if last_spoken in turns:
            spoken = previous_turn - turns[last_spoken]
        else:
            spoken = 0
        
        #updating new turn
        turns[last_spoken] = previous_turn
        last_spoken = spoken
    
    return last_spoken

part1 = elfGame(2020)
print('part1:', part1)
assert(part1 == 700)

print('calulating turn2...')
t1 = time()
part2 = elfGame(30000000)
t2 = time()
print('part2:', part2, 'took', t2-t1, 'seconds')
assert(part2 == 51358)
