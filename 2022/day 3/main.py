file = open('input.txt', 'r')
Lines = [line.strip() for line in file.readlines()]

part1 = 0
part2 = 0

def priority(char):
    if char.islower():
        return ord(char)-96
    else: 
        return ord(char)-38

for i, line in enumerate(Lines):
    #Part 1
    half = int(len(line) / 2)
    common = list(set(line[half:]) & set(line[:half]))[0]
    part1 += priority(common)
    #Part 2
    if i % 3 == 0:
        common = list(set(Lines[i]) & set(Lines[i+1]) & set(Lines[i+2]))[0]
        part2 += priority(common)
print("Part 1: " + str(part1))
print("Part 2: " + str(part2))