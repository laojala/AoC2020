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
