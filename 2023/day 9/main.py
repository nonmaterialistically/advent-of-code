import os
from collections import defaultdict
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open("input.txt", "r") as file:
    lines = file.readlines()

d = defaultdict(list)
for i, line in enumerate(lines):
    line = line.strip()
    d[i].append([int(value) for value in re.findall(r"\-?\d+", line)])
    k=0
    while not all(difference == 0 for difference in d[i][-1]):
        d[i].append([d[i][k][j+1]-d[i][k][j] for j in range(len(d[i][k])-1)])
        k += 1

for sequence in d.values():
    for i in reversed(range(len(sequence)-1)):
        sequence[i].append(sequence[i][-1]+sequence[i+1][-1])
        sequence[i].insert(0, sequence[i][0]-sequence[i+1][0])

part1 = 0
part2 = 0
for sequence in d.values():
    part1 += sequence[0][-1]
    part2 += sequence[0][0]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")