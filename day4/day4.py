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

valid_passports = 0

for document in passports:
    if {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'} <= set(document):
        valid_passports = valid_passports + 1

print(valid_passports)





