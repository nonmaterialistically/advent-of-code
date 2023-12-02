import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open("input.txt", "r") as file:
    lines = file.readlines()

possible_games = []
game_sets_power = 0

for line in lines:
    game_id, game_sets = line.strip().split(":")
    game_id = int(game_id.split(" ")[1])
    game_sets = game_sets.split(";")
    possible_games.append(game_id)
    cubes = {}
    highest = {"red": 0, "green": 0, "blue": 0}
    for game_set in game_sets:
        pattern = re.compile(r'(\d+) (\w+)')
        for (number, cubes) in re.findall(pattern, game_set):
            if (cubes == "red" and int(number) > 12) or (cubes == "green" and int(number) > 13) or (cubes == "blue" and int(number) > 14):
                if game_id in possible_games:
                    possible_games.remove(game_id)
            if int(number) > highest[cubes.strip()]:    
                highest[cubes.strip()] = int(number)
    existing_cubes = [number for number in highest.values() if number > 0]
    hightest_multiple = 1
    for value in existing_cubes:
        hightest_multiple *= value
    game_sets_power += hightest_multiple
print(f"Part1: {sum(possible_games)}")
print(f"Part2: {game_sets_power}")
