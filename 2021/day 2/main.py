file = open('input.txt', 'r')
Lines = file.readlines()

horizontal = 0
depth = 0
aim = 0

for line in Lines:
    instruction = line.strip().split()[0]
    value = int(line.strip().split()[1])
    if instruction == 'forward':
        horizontal += value
    if instruction == 'down':
        depth += value
    if instruction == 'up':
        depth -= value

print("Part 1: ", horizontal*depth)

horizontal = 0
depth = 0
aim = 0

for line in Lines:
    instruction = line.strip().split()[0]
    value = int(line.strip().split()[1])
    if instruction == 'forward':
        horizontal += value
        depth += value*aim
    if instruction == 'down':
        aim += value
    if instruction == 'up':
        aim -= value

print("Part 2: ", horizontal*depth)