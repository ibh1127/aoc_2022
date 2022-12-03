def get_char_int(character):
    if character.isupper():
        return ord(character) - 38
    if character.islower():
        return ord(character) - 96

sacks = input.split("\n")

n = 3
groups_of_3 = [sacks[i * n:(i + 1) * n] for i in range((len(sacks) + n - 1) // n )]

running_total = 0

for group in groups_of_3:
    for sack in group:
        for item in sack:
            if item in group[1] and item in group[2]:
                running_total += get_char_int(item)
                break
        break

print(running_total) 




