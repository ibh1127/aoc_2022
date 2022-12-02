score_key = {"X": 1, "Y":2, "Z": 3}

wins = ["A Y", "B Z", "C X"]
ties = ["A X", "B Y", "C Z"]

rounds = input.split("\n")

running_score = 0
for r in rounds:
    if r:
        if r in wins:
            running_score += 6
        if r in ties:
            running_score += 3

        running_score += score_key[r.split(" ")[1]]

print(running_score)

