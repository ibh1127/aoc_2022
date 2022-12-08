grid = []
lines = input.split("\n")
scores = []

def score_from_above(tree_value, row_index, column_index):
    offset = 1
    trees_score = 0
    while (row_index - offset) >= 0:
        tree_above_value = grid[row_index - offset][column_index]
        if tree_above_value >= tree_value:
            trees_score += 1
            break
        else:
            trees_score += 1
        offset += 1

    return trees_score

def score_from_below(tree_value, row_index, column_index):
    offset = 1
    trees_score = 0
    while (row_index + offset) <= 98:
        tree_below_value = grid[row_index + offset][column_index]
        if tree_below_value >= tree_value:
            trees_score += 1
            break
        else:
            trees_score += 1
        offset += 1

    return trees_score

def score_from_right(tree_value, row_index, column_index):
    offset = 1
    trees_score = 0
    while (column_index + offset) <= 98:
        tree_right_value = grid[row_index][column_index + offset]
        if tree_right_value >= tree_value:
            trees_score += 1
            break
        else:
            trees_score += 1
        offset += 1

    return trees_score

def score_from_left(tree_value, row_index, column_index):
    offset = 1
    trees_score = 0
    while (column_index - offset) >= 0:
        tree_left_value = grid[row_index][column_index - offset]
        if tree_left_value >= tree_value:
            trees_score += 1
            break
        else:
            trees_score += 1
        offset += 1

    return trees_score

def get_score(row_index,column_index):
    tree_value = grid[row_index][column_index]

    above_score = score_from_above(tree_value, row_index, column_index)
    below_score = score_from_below(tree_value, row_index, column_index)
    right_score = score_from_right(tree_value, row_index, column_index)
    left_score = score_from_left(tree_value, row_index, column_index)
        
    return above_score * below_score * right_score * left_score

for l in lines:
    row = [t for t in l]
    grid.append(row)

row_index = 0
for row in grid:
    column_index = 0
    for column in row:
        score = get_score(row_index, column_index)
        scores.append(score)
        column_index += 1
    row_index += 1

scores.sort()
print(scores[len(scores) - 1])




