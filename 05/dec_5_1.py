raw_data = crate_input.replace("["," ").replace("]", " ").split("\n")
row_length = len(raw_data[0])
column_count = (row_length + 1)/4
crate_stacks = [[] for _ in range(9)]


def hydrate_stacks():
    for row in raw_data:
        rolling_index = 1
        for s in crate_stacks:
            next_letter = row[rolling_index]
            if next_letter != " ":
                s.append(next_letter)
            rolling_index += 4

    for s in crate_stacks:
        s.reverse()
        print(s)

def move_crates():
    instructions = input_instructions.split("\n")
    for line in instructions:
        parsed_line = line.split(" ")
        print(parsed_line)

        quantity = int(parsed_line[1])
        source = int(parsed_line[3]) - 1
        target = int(parsed_line[5]) - 1

        for q in range(quantity):
            source_column = crate_stacks[source]
            target_column = crate_stacks[target]

            source_top_crate = source_column.pop(len(source_column) - 1)
            target_column.append(source_top_crate)

    for c in crate_stacks:
        print(c[len(c) - 1])

hydrate_stacks()
move_crates()