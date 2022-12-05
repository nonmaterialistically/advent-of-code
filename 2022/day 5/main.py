import re

file = open('input.txt', 'r')
Lines = [line for line in file.readlines()]

part1 = ""
part2 = ""

divider = Lines.index("\n")
crates_rows = [re.split("    | ",line[:-1]) for line in Lines[:divider-1]]
stacks = str(Lines[divider-1:divider][0]).strip().split("   ")
crates = [[re.sub('\[|\]','',row[int(n)-1]) for row in crates_rows if row[int(n)-1] ] for n in stacks]
moves = [line.strip() for line in Lines[divider+1:]]

crates1 = [list[:] for list in crates]
crates2 = [list[:] for list in crates]

for move in moves:
    search = re.search('move (\d+) from (\d) to (\d)', move)
    quantity,f,t = int(search.group(1)),int(search.group(2)),int(search.group(3))
    #Part1
    for _ in range(quantity):
        crates1[t-1].insert(0, crates1[f-1][0])
        crates1[f-1].pop(0)
    #Part2
    crates2[t-1] = crates2[f-1][0:quantity] + crates2[t-1]
    del crates2[f-1][:quantity]
#Part1
for crate in crates1:
    if bool(crate):
        part1 += crate[0]
print(part1)

#Part2
for crate in crates2:
    if bool(crate):
        part2 += crate[0]
print(part2)