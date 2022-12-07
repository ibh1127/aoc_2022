file_inventory = {}
directory_invetory = set()
lines = input.split("\n")
current_dir = ""
sum = 0

def move_up_to_parent(l):
    global current_dir
    current_dir_split = current_dir.split("/")
    del(current_dir_split[len(current_dir_split) - 2])
    current_dir = '/'.join([str(dirname) for dirname in current_dir_split])
    current_dir = current_dir.replace('//','/')

def move_down_to_child(line_words):
    global current_dir
    if current_dir != "/":
        current_dir += line_words[2] + "/"
    else:
        current_dir += ("/" + line_words[2] + "/")
    current_dir = current_dir.replace('//','/')

def check_containment(dir_name, file_name):
    index = 0
    for character in dir_name:
        if character != file_name[index]:
            return False
        index += 1
    return True
    
for l in lines:
    line_words = l.split(" ")
    first_word = line_words[0]

    if first_word == "$":
        if "cd .." in l:
            move_up_to_parent(l)
        elif "cd" in l:
            move_down_to_child(line_words)
        else:
            continue

    elif first_word == "dir":
        directory_invetory.add(current_dir)
    else:
        file_name = line_words[1]
        file_size = line_words[0]
        file_inventory[current_dir + file_name] = file_size
        directory_invetory.add(current_dir)

for d in directory_invetory:
    dir_size_total = 0
    for k,v in file_inventory.items():
        if check_containment(d,k):
            dir_size_total += int(v)

    if dir_size_total <= 100000:
            sum += dir_size_total

print(sum)


    
