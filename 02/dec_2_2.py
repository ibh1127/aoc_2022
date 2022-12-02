score_key = {"X": 1, "Y":2, "Z": 3}

wins = ["A Y", "B Z", "C X"]
ties = ["A X", "B Y", "C Z"]
loses = ["A Z", "B X", "C Y"]

def mutate_round(round):
    opponent_hand = round.split(" ")[0]

    if "X" in round:
        for l in loses:
            if opponent_hand in l:
                return l
            
    if "Y" in round:
        for t in ties:
            if opponent_hand in t:
                return t
    if "Z" in round:
        for w in wins:
            if opponent_hand in w:
                return w


rounds = input.split("\n")

running_score = 0
for r in rounds:
    if r:
        r = mutate_round(r)
        if r in wins:
            running_score += 6
        if r in ties:
            running_score += 3

        running_score += score_key[r.split(" ")[1]]

print(running_score)

