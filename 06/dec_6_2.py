index = 0

for character in input:
    current_slice = input[index:index + 14]
    duplicate_detected = False
    for c in current_slice:
        occurences = current_slice.count(c)
        if occurences > 1:
            duplicate_detected = True
            index += 1
            break

    if not duplicate_detected:
        print(current_slice)
        print(index + 14)
        break