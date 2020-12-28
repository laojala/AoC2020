with open('day10.data','r') as f:
    data = f.read().splitlines()
    data = [int(i) for i in data]

device = max(data) + 3
data.append(device)
data.append(0)

data.sort()

jolt1 = []
jolt3 = []

for index, adapter in enumerate(data):

    if index == len(data) - 1:
        break
    
    difference = data[index+1] - adapter

    if difference == 1:
        jolt1.append(adapter)
    if difference == 3:
        jolt3.append(adapter)
    if difference == 2:
        print('two')

print('part1:', len(jolt1) * len(jolt3))
assert(len(jolt1) * len(jolt3)== 2470)

#part 2 solution is strongly inspired by https://github.com/q-viper/Adevent-Of-Code-2020
#author's blog: https://dev.to/qviper/advent-of-code-2020-python-solution-day-10-30kd

data.remove(0)

routes = {0:1}
for line in data:
    routes[line] = 0
    if line - 1 in routes:
        routes[line]+=routes[line-1]
    if line - 2 in routes:
        routes[line]+=routes[line-2]
    if line - 3 in routes:
        routes[line]+=routes[line-3]

print('part2', routes[max(data)])
assert(routes[max(data)] == 1973822685184)
