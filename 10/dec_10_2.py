cycles = 0
regx = 1
lines = input.split("\n")
crt_line = ""

def check_cycles(sprite_range):
    global crt_line
    global cycles
    if cycles in [40]:
        print(crt_line)
        crt_line = ""
        cycles = 0
    if cycles in sprite_range:
        crt_line += "#"
    else:
        crt_line += "."

sprite_range = [regx - 1, regx, regx + 1]
check_cycles(sprite_range)

for l in lines:
    if l.split(" ")[0] == "noop":
        cycles += 1
        check_cycles(sprite_range)
    if l.split(" ")[0] == "addx":
        val = int(l.split(" ")[1])
        cycles += 1
        check_cycles(sprite_range)
        cycles += 1
        regx += int(val)
        sprite_range = [regx - 1, regx, regx + 1]
        check_cycles(sprite_range)


