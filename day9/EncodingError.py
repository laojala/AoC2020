with open('day9.data','r') as f:
    data = f.read().splitlines()
    data = [int(i) for i in data]


preamble = 25
number = None

for i in range(preamble, len(data)):
    number = data[i]
    set = data[i-preamble:i]

    is_in_set = True  # expecting that every number is valid

    for n in set:
        expected = number - n

        if n == expected:
            continue  #can't be a same number
        is_in_set = expected in set
        if is_in_set:
            break

    if not is_in_set: # break if number is not valid
        print('part1:', number)
        assert(number == 22406676)
        break  

#part2
list_found = False

for index , n in enumerate(data):
    
    sum = 0

    if list_found:
        print('part2:', min(list) + max(list))
        assert(min(list) + max(list) == 2942387)
        break

    list = []

    for i in range(index+1, len(data)-1):
        sum += data[i]
        list.append(data[i])

        if sum == number and len(list) >= 2:
            list_found = True
            break
    
        if sum > number:
            break
