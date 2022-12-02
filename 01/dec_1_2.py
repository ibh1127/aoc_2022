elves = input.split("\n\n")

totals = []
for e in elves:
    running_total = 0
    calories_counts = e.split("\n")
    for c in calories_counts:
        if c:
            running_total += int(c)

    totals.append(running_total)

totals.sort(reverse=True)
print(sum(totals[:3]))

    

