file = open('input.txt', 'r')
Lines = [line.strip() for line in file.readlines()]

X = 1
cycle = 1
V = 0
steps = 0
current_op = 0
part1 = []
part2 = ""

while current_op < len(Lines)+1:
    #Part1
    if cycle in [20, 60, 100, 140, 180, 220]:
        part1.append(X*cycle)
    if cycle % 40 == 0:
        print(part2)
        part2 = ""
    if cycle == 1:
        part2 = "#"
    if steps > 0:
        X += V
        V = 0
        steps -= 1
    else:
        if current_op < len(Lines):
            line = Lines[current_op]
            if line.startswith("addx"):
                V = int(line[5:])
                steps += 1
        current_op += 1
    #Part2
    if cycle % 40 in [X-1, X, X+1]:
        part2 = part2 + "#"
    else:
        part2 = part2 + "."
    cycle += 1
print("Part1: "+str(sum(part1)))