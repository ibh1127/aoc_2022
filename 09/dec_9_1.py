instructions = input.split('\n')
head = [0,0]
tail = [0,0]
history = set()

def move_up(knot):
    knot[1] += 1

def move_down(knot):
    knot[1] -= 1

def move_left(knot):
    knot[0] -= 1

def move_right(knot):
    knot[0] += 1

def evaluate_positions(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]

    if x_diff == 0 and y_diff > 1:
        move_up(tail)
    elif x_diff == 0 and y_diff < -1:
        move_down(tail)
    elif x_diff < -1 and y_diff == 0:
        move_left(tail)
    elif x_diff > 1 and y_diff == 0:
        move_right(tail)
    elif (x_diff == -1 and y_diff == 2) or (x_diff == -2 and y_diff == 1):
        move_up(tail)
        move_left(tail)
    elif (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1):
        move_up(tail)
        move_right(tail)
    elif (x_diff == 1 and y_diff == -2) or (x_diff == 2 and y_diff == -1):
        move_down(tail)
        move_right(tail)
    elif (x_diff == -1 and y_diff == -2) or (x_diff == -2 and y_diff == -1):
        move_down(tail)
        move_left(tail)

def append_tail_history(tail):
    history.add(str(tail))
    
append_tail_history(tail)

for i in instructions:
    direction = i.split(" ")[0]
    spaces = int(i.split(" ")[1])

    for r in range(spaces):
        if direction == "U":
            move_up(head)
        elif direction == "D":
            move_down(head)
        elif direction == "L":
            move_left(head)
        elif direction == "R":
            move_right(head)

        evaluate_positions(head, tail)
        append_tail_history(tail)

print(len(history))
    


