import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open("input.txt", "r") as file:
    lines = file.readlines()

part1_digits = []
part2_digits = []
part1_sum = 0
part2_sum = 0
valid_text_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in lines:
    line_reconstructed = ""
    part1_digits = []   
    part2_digits = []
    for char in line:
        line_reconstructed += char
        if char.isdigit():
            part1_digits.append(int(char))
            part2_digits.append(int(char))
        if any(text_digit in line_reconstructed for text_digit in valid_text_digits):
            for digit in valid_text_digits:
                if digit in line_reconstructed:
                    part2_digits.append(valid_text_digits.index(digit)+1)
            line_reconstructed = f"{line_reconstructed[-1]}"
    if len(part1_digits) > 0:
        part1_sum += int(f"{part1_digits[0]}{part1_digits[-1]}")
    if len(part2_digits) > 0:
        part2_sum += int(f"{part2_digits[0]}{part2_digits[-1]}")

print(f"Part 1: {part1_sum}")
print(f"Part 2: {part2_sum}")
