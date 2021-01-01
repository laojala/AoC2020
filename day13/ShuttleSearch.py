from math import ceil

timestamp = 1008833
#busses = [7,13,'x','x',59,'x',31,19]
departures = [19,'x','x','x','x','x','x','x','x',41,'x','x','x','x','x','x','x','x','x',643,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',17,13,'x','x','x','x',23,'x','x','x','x','x','x','x',509,'x','x','x','x','x',37,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',29]

### PART1
#filter out strings
busses = list(filter(lambda x : isinstance(x, int), departures))

wait_times = {}

for bus in busses:
    wait_time =  (bus * ceil(timestamp / bus)) - timestamp
    wait_times[bus] = wait_time

#find min value
min = min(wait_times.items(), key=lambda x: x[1])
part1 = min[0] * min[1]
print('part1:', part1)
assert(part1 == 2545)

### PART2
hint: https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Existence_(constructive_proof)