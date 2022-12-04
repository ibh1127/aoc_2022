running_total = 0

def check_overlap(pair_ranges):
    section_list_1 = pair_ranges[0]
    section_list_2 = pair_ranges[1]

    if all(section in section_list_1 for section in section_list_2):
        return True
    if all(section in section_list_2 for section in section_list_1):
        return True
    return False

section_pairs = input.split("\n")

for pair in section_pairs:
    pair_range_list = []
    section_ranges = pair.split(',')

    for section_range in section_ranges:
        section_range_list = [*range(int(section_range.split('-')[0]), int(section_range.split('-')[1]) + 1)]
        pair_range_list.append(section_range_list)
    
    if check_overlap(pair_range_list):
        running_total += 1

print(running_total)





