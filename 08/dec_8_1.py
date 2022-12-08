grid = []
lines = input.split("\n")
total_visible = 0

def visible_from_above(tree_value, row_index, column_index):
    offset = 1
    while (row_index - offset) >= 0:
        tree_above_value = grid[row_index - offset][column_index]
        if tree_above_value >= tree_value:
            return False
        offset += 1
    return True

def visible_from_below(tree_value, row_index, column_index):
    offset = 1
    while (row_index + offset) <= 98:
        tree_below_value = grid[row_index + offset][column_index]
        if tree_below_value >= tree_value:
            return False
        offset += 1
    return True

def visible_from_right(tree_value, row_index, column_index):
    offset = 1
    while (column_index + offset) <= 98:
        tree_right_value = grid[row_index][column_index + offset]
        if tree_right_value >= tree_value:
            return False
        offset += 1
    return True

def visible_from_left(tree_value, row_index, column_index):
    offset = 1
    while (column_index - offset) >= 0:
        tree_left_value = grid[row_index][column_index - offset]
        if tree_left_value >= tree_value:
            return False
        offset += 1
    return True

def is_visible(row_index,column_index):
    tree_value = grid[row_index][column_index]

    if (row_index == 0 or column_index == 0) or (row_index == 98 or column_index == 98):
        return True

    if visible_from_above(tree_value, row_index, column_index):
        return True
    if visible_from_below(tree_value, row_index, column_index):
        return True
    if visible_from_right(tree_value, row_index, column_index):
        return True
    if visible_from_left(tree_value, row_index, column_index):
        return True

    return False

for l in lines:
    row = [t for t in l]
    grid.append(row)

row_index = 0
for row in grid:
    column_index = 0
    for column in row:
        if is_visible(row_index, column_index):
            total_visible += 1
        column_index += 1
    row_index += 1

print(total_visible)




