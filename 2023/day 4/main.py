import os
from collections import defaultdict
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open("input.txt", "r") as file:
    lines = file.readlines()

part1 = 0
part2 = 0
copies = defaultdict(int)
cards = []

for line in lines:
    line = line.strip()
    card_n = line.split(":")[0].split(" ")[-1].strip()
    winning_numbers = []
    my_numbers = []
    numbers_i_have = []
    winning_numbers, my_numbers = line.split(":")[1].split("|")
    winning_numbers = re.findall(r'\d+', winning_numbers)
    my_numbers = re.findall(r'\d+', my_numbers)
    numbers_i_have = [number for number in my_numbers if number in winning_numbers]
    cards.append((int(card_n), winning_numbers, my_numbers, numbers_i_have))

for i,card in enumerate(cards):
    copies[i] += 1
    card_n = card[0]
    numbers_i_have = card[3]
    if len(numbers_i_have) > 0:
        value = 1
        for number in range(len(numbers_i_have)-1):
            value *= 2
        part1 += value
        for n in range(len(numbers_i_have)):
            #print(f"Counting card {i}, adding {copies[i]} copies of card {i+n+1}")
            copies[i+n+1] += copies[i]

print(f"Part 1: {part1}")
print(f"Part 2: {sum(copies.values())}")