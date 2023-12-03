import os
from collections import defaultdict

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open("input.txt", "r") as file:
    lines = file.readlines()

part_number = 0
symbols = []
part1 = 0
part2 = 0
gears_positions = set()
num_adjecent_to_gears = defaultdict(list)
found_symbol = False

for line in lines:
    for char in line.strip():
        if not char.isdigit() and char != ".":
            symbols.append(char)

for y, line in enumerate(lines):
    part_number = 0
    gears_positions = set()
    for x, char in enumerate(line):
        if char.isdigit():
            part_number = part_number*10+int(char)
            for yy in [-1, 0, 1]:
                for xx in [-1, 0, 1]:
                    if 0<=y+yy<len(lines) and 0<=x+xx<len(line):
                        if not lines[y+yy][x+xx].isdigit() and lines[y+yy][x+xx] != ".":
                            found_symbol = True
                        if lines[y+yy][x+xx] == "*":
                            gears_positions.add((x+xx, y+yy))
        elif part_number>0:
            if found_symbol:
                part1 += part_number
            for pos in gears_positions:
                num_adjecent_to_gears[pos].append(part_number)
            part_number = 0
            found_symbol = False
            gears_positions = set()

for k, v in num_adjecent_to_gears.items():
    if len(v) > 1:
        part2 += v[0]*v[1]
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
