data = []

f=open("input.dat","r")
for line in f:
    data.append(int(line.strip('\n')))

result = 2020
needed = 0

for item in data:
    needed_number = result-item
    if needed_number in data:
        print("Part1 result:", item*needed_number)
        break

#second part

ready = False

for index,number1 in enumerate(data):
    for second_index in range(index+1, len(data)):
        needed_number = result - number1 - data[second_index]
        if needed_number in data:
            print("Part2 result:", number1*data[second_index]*needed_number)
            break

