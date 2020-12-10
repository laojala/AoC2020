import re

#read test data and convert it as list containing dictionaries

all_lines = []

with open('day4.dat','r') as f:
    all_lines = f.readlines()

passports = []

last_line = len(all_lines)
entry = []

for index,line in enumerate(all_lines):

    if line != '\n':
        entry.extend(line.split())
    
    if line == '\n' or index == last_line-1:
        dictionary = dict(element.split(':') for element in entry)
        passports.append(dictionary)
        entry = []

##PART1: does travel document contain required keys?

valid_passports_part1 = 0

for document in passports:
    if {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'} <= set(document):
        valid_passports_part1 = valid_passports_part1 + 1

assert(valid_passports_part1 == 182)
print('part 1:', valid_passports_part1)


##PART2 does values of required keys conform to rules

valid_passports_part2 = 0

def validRange(element, low, up):
    if (int(element) >= low and int(element) <= up):
        return True

for document in passports:
    if {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'} <= set(document):
        if not validRange(document['byr'], 1920, 2002):
            continue
        if not validRange(document['iyr'], 2010, 2020):
            continue
        if not validRange(document['eyr'], 2020, 2030):
            continue
        if not (document['hgt'][-2:] == 'cm' or document['hgt'][-2:] == 'in'):
            continue
        if document['hgt'][-2:] == 'cm':
            if not validRange(document['hgt'][:-2], 150, 193):
                continue
        if document['hgt'][-2:] == 'in':
            if not validRange(document['hgt'][:-2], 59, 76):
                continue
        if not re.match('^#(?:[0-9a-fA-F]{3}){1,2}$', document['hcl']):
            continue
        if not document['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        if not re.match('^\\d{9}$', document['pid']):
            continue

        valid_passports_part2 = valid_passports_part2 + 1

assert(valid_passports_part2 == 109)
print('part 2:', valid_passports_part2)
