import os
from collections import defaultdict
import re
import math

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open("input.txt", "r") as file:
    lines = file.readlines()

time = [int(n) for n in re.findall("\d+", lines[0].strip())]
distance = [int(n) for n in re.findall("\d+", lines[1].strip())]

part1 = defaultdict(int)

for i in range(len(time)):
    max_t = time[i]
    record_d = distance[i]
    for x in range(max_t):
        d = x * (max_t - x)
        if d > record_d:
            part1[i] += 1

print(f"Part 1: {math.prod([win for win in part1.values()])}")

time = int("".join(n for n in re.findall("\d+", lines[0].strip())))
distance = int("".join(n for n in re.findall("\d+", lines[1].strip())))
part2 = 0

for x in range(time):
    d = x * (time - x)
    if d > distance:
        part2 += 1

print(f"Part 2: {part2}")