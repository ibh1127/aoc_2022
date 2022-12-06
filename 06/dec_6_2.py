index = 0

for character in input:
    current_slice = input[index:index + 14]
    duplicate_detected = False
    for c in current_slice:
        occurences = current_slice.count(c)
        if occurences > 1:
            duplicate_detected = True
            break

    if duplicate_detected:
        index += 1
        continue
    else:
        print(current_slice)
        print(index + 14)
        break