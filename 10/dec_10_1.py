cycles = 1
regx = 1
strengths = []

lines = input.split("\n")

def check_cycles():
    if cycles in(20,60,100,140,180,220):
        strengths.append(cycles * regx)


for l in lines:
    if l.split(" ")[0] == "noop":
        cycles += 1
        check_cycles()
    if l.split(" ")[0] == "addx":
        val = int(l.split(" ")[1])
        cycles += 1
        check_cycles()
        cycles += 1
        regx += int(val)
        check_cycles()

print(sum(strengths))

