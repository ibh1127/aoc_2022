elves = input.split("\n\n")

max = 0
for e in elves:
    running_total = 0
    calories_counts = e.split("\n")
    for c in calories_counts:
        if c:
            running_total += int(c)
    if max < running_total:
        max = running_total

print(max)

    

