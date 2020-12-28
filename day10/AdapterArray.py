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

print('part1:', len(jolt1) * len(jolt3))
assert(len(jolt1) * len(jolt3)== 2470)