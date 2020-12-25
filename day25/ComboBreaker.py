
card = 14012298
door = 74241

value = 1
loops_for_card = 0
loops_for_door = 0

while value != card:
    loops_for_card = loops_for_card + 1
    value = (value * 7) % 20201227

encryption_key = 1

for x in range(loops_for_card):
    encryption_key = (encryption_key * door) % 20201227

print(encryption_key)
assert(encryption_key == 18608573)