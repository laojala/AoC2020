rules =  {}

#read input data to dictionary
with open('day7.data','r') as f:
    data = f.read().splitlines()

    for line in data:
        outer_bag = line.partition(' bags contain ')[0]
        inner_text = line.partition(' bags contain ')[2]

        inner = {}

        if inner_text == 'no other bags.':
            rules[outer_bag] = inner
            continue
        
        inner_list = inner_text.split(',')

        for item in inner_list:
            item = item.strip()
            number = int(item.partition(' ')[0])
            colour = item.partition(' ')[2]
            colour = colour.split(' ')[0] + ' ' + colour.split(' ')[1]
            inner[colour] = number

        rules[outer_bag] = inner

def countBagsContaining(ruleset, colour):

    outer_bags = []

    for rule in ruleset:
        if colour in ruleset[rule]:
            outer_bags.append(rule)
    
    return outer_bags
        
#part 1
colours = ['shiny gold']
all_handled = False
handled = []

while not all_handled:

    for item in colours:

        new_bags = []

        if item not in handled:
            new_bags = countBagsContaining(rules, item)
        
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
