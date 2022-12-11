import re
import math
import copy

file = open('input.txt', 'r')
Lines = [line.strip() for line in file.readlines()]

monkeys = dict()
round = 0

#create initial monkey db
for line in Lines:
    if line.startswith("Monkey "):
        n = line[-2]
        monkeys[n] = dict()
        monkeys[n]["inspect counter"] = 0
    if line.startswith("Starting items:"):
        monkeys[n]["items"] = [int(item) for item in re.search('Starting items: ([\d, ]+)', line).group(1).split(", ")]
    if line.startswith("Operation:"):
        monkeys[n]["operation"] = re.search('Operation: new = (.*)', line).group(1).strip()
    if line.startswith("Test:"):
        monkeys[n]["divisible by"] = int(re.search('Test: divisible by (\d+)', line).group(1))
    if line.startswith("If true:") or line.startswith("If false:"):
        search = re.search('If (\w+): throw to monkey (\d+)', line)
        monkeys[n][search.group(1)] = search.group(2)

lcm = 1
lcm = math.lcm(*[monkeys[n]["divisible by"] for n in monkeys])

monkeys_copy = copy.deepcopy(monkeys)

for part in [1, 2]:
    round = 0 
    while round < 20 if part == 1 else round < 10000:
        round += 1
        for n in monkeys:
            for item in [item for item in monkeys[n]["items"]]:
                old = item
                item = eval(monkeys[n]["operation"])
                monkeys[n]["inspect counter"] += 1
                if part == 1:
                    item = item//3
                if part == 2:
                    item = item%lcm
                if item%monkeys[n]["divisible by"] == 0:
                    monkeys[monkeys[n]["true"]]["items"].append(item)
                    monkeys[n]["items"].remove(old)
                else:
                    monkeys[monkeys[n]["false"]]["items"].append(item)
                    monkeys[n]["items"].remove(old)
    if round == 20 and part == 1:
        result = sorted([monkeys[n]["inspect counter"] for n in monkeys], reverse=True)
        result = result[0]*result[1]
        print(result)
        monkeys = copy.deepcopy(monkeys_copy)
    if round == 10000 and part == 2:
        result = sorted([monkeys[n]["inspect counter"] for n in monkeys], reverse=True)
        result = result[0]*result[1]
        print(result)