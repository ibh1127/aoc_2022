from math import gcd
from functools import reduce

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

rounds = 10000
divs = []
lines = input.split("\n")
monkeys = []

def hydrate_monkeys():
    for l in lines:
        if "Monkey" in l:
            monkey = {}
            monkey["name"] = l
            monkeys.append(monkey)
            monkey["count"] = 0
        if "Starting" in l:
            monkey["items"] = l.split(':')[1].split(',')
        if "Operation" in l:
            monkey["inspect"] = l.split(": ")[1]
        if "Test" in l:
            monkey["test"] = l
            divs.append(int(l.split(" ")[-1:][0]))
        if "true" in l:
            monkey["true_test"] = l
        if "false" in l:
            monkey["false_test"] = l

def reduce_monkey_item(current_item):

    current_item = current_item % lcm_num
    return current_item

hydrate_monkeys()
lcm_num = lcm(divs)


for r in range(rounds):
    for m in monkeys:
        if m["items"]:
            for i in range(len(m["items"])):
                m["count"] += 1
                current_item = int(m["items"].pop(0))
                if "* old" in m["inspect"]:
                    new_stress = current_item * current_item
                elif "*" in m["inspect"]:
                    new_stress = current_item * int(m["inspect"].split(" ")[4])
                else:
                    new_stress = current_item + int(m["inspect"].split(" ")[4])

                if new_stress % int(m["test"].split(" ")[-1:][0]) == 0:
                    throw_to_monkey = int(m["true_test"].split(" ")[-1:][0])
                else:
                    throw_to_monkey = int(m["false_test"].split(" ")[-1:][0])

                monkeys[throw_to_monkey]["items"].append(new_stress)

    for m in monkeys:
        for i in range(len(m["items"])):
            if m["items"][i] > lcm_num:
                m["items"][i] = reduce_monkey_item(m["items"][i])

shenanigans = []

for m in monkeys:
    shenanigans.append(m["count"])

shenanigans.sort(reverse=True)

print(shenanigans[0] * shenanigans[1])






        






    