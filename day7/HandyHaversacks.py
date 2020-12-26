rules =  {}

#read input data to dictionary containing tuples
with open('day7.data','r') as f:
    data = f.read().splitlines()

    for line in data:
        outer_bag = line.partition(' bags contain ')[0]
        inner_text = line.partition(' bags contain ')[2]

        inner = []

        if inner_text == 'no other bags.':
            rules[outer_bag] = inner
            continue
        
        inner_list = inner_text.split(',')

        for item in inner_list:
            item = item.strip()
            number = int(item.partition(' ')[0])
            colour = item.partition(' ')[2]
            colour = colour.split(' ')[0] + ' ' + colour.split(' ')[1]
            inner.append((colour, number))

        rules[outer_bag] = inner


# part 1
colours = ['shiny gold']
all_handled = False
handled = []

while not all_handled:

    for item in colours:

        new_bags = []

        if item not in handled:
            #add new colors from rules:
            for rule in rules:
                for colour in rules[rule]:
                    if item in colour:
                        new_bags.append(rule)
                
        if item != 'shiny gold':
            handled.append(item)

        if len(new_bags) == 0:
            all_handled = True

        for new in new_bags:
            if new not in colours:
                colours.append(new)

part1 = len(handled)
assert(part1 == 229)
print('part1', part1)


# part 2, inspired by: https://github.com/sijmn/aoc2020/blob/master/python/day07.py
part2 = 0
stack = [("shiny gold", 1)]
while stack:
    color, n = stack.pop()
    part2 += n

    children = rules[color]

    for child, m in children:
        stack.append((child, n * m))
part2 -= 1

print("part 2:", part2)
assert (part2 == 6683)