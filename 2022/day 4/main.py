file = open('input.txt', 'r')
Lines = [line.strip() for line in file.readlines()]

part1 = 0
part2 = 0

for line in Lines:
    first_range = list(map(int, line.split(",")[0].split("-")))
    second_range = list(map(int, line.split(",")[1].split("-")))
    first_exp = [n for n in range(first_range[0], first_range[1]+1)]
    second_exp = [n for n in range(second_range[0], second_range[1]+1)]
    if (set(first_exp).issubset(set(second_exp))) or (set(second_exp).issubset(set(first_exp))): #I'll just ignore the order since they are ranges
        part1 += 1
    if (set(first_exp) & set(second_exp)):
        part2 += 1
print(part1)
print(part2)