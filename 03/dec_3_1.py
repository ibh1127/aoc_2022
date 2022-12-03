def get_char_int(character):
    if character.isupper():
        return ord(character) - 38
    if character.islower():
        return ord(character) - 96

sacks = input.split("\n")

running_total = 0

for s in sacks:
    if s:
        middle = int(len(s)/2)

        compartment_left = s[:middle]
        compartment_right = s[middle:]

        for item in compartment_left:
            if item in compartment_right:
                running_total += get_char_int(item)
                break

print(running_total)



