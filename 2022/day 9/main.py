import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open("input.txt", "r") as file:
    lines = file.readlines()

motions = [line.strip() for line in lines]

# Remember that in the first part, knots[0] is the head and knots[1] is the tail
# In the second part, knots[0] is the head and knots[9] is the tail
knots = []
for n in range(10):
    knots.append([0, 0])

knot_1_visited = set()
knot_1_visited.add(tuple(knots[1]))
knot_9_visited = set()
knot_9_visited.add(tuple(knots[9]))

for motion in motions:
    direction = motion.split(" ")[0]
    distance = int(motion.split(" ")[1])
    for _ in range(distance):
        if direction == "R":
            knots[0][0] += 1
        elif direction == "L":
            knots[0][0] -= 1
        elif direction == "U":
            knots[0][1] += 1
        elif direction == "D":
            knots[0][1] -= 1
        # Iterate over all following knots (skip the head)
        # ALL of this would probably be cleaner if I used a dictionary instead of a list
        for n, knot in enumerate(knots):
            if n == 0:
                continue
            # Check if H and T are more than 1 cell far from each other
            if abs(knots[n][0] - knots[n-1][0]) > 1 or abs(knots[n][1] - knots[n-1][1]) > 1:
                if knots[n-1][0] != knots[n][0] and knots[n-1][1] != knots[n][1]:
                    if knots[n-1][0] > knots[n][0] and knots[n-1][1] > knots[n][1]:
                        knots[n][0] += 1
                        knots[n][1] += 1
                    elif knots[n-1][0] < knots[n][0] and knots[n-1][1] < knots[n][1]:
                        knots[n][0] -= 1
                        knots[n][1] -= 1
                    elif knots[n-1][0] > knots[n][0] and knots[n-1][1] < knots[n][1]:
                        knots[n][0] += 1
                        knots[n][1] -= 1
                    elif knots[n-1][0] < knots[n][0] and knots[n-1][1] > knots[n][1]:
                        knots[n][0] -= 1
                        knots[n][1] += 1
                else:
                    if abs(knots[n-1][0] - knots[n][0]) > 1:
                        if knots[n-1][0] > knots[n][0]:
                            knots[n][0] += 1
                        elif knots[n-1][0] < knots[n][0]:
                            knots[n][0] -= 1
                    if abs(knots[n-1][1] - knots[n][1]) > 1:
                        if knots[n-1][1] > knots[n][1]:
                            knots[n][1] += 1
                        elif knots[n-1][1] < knots[n][1]:
                            knots[n][1] -= 1
        knot_1_visited.add(tuple(knots[1]))
        knot_9_visited.add(tuple(knots[9]))

print(f"Part 1 (visited by tail): {len(knot_1_visited)}")
print(f"Part 2 (visited by knot number 9): {len(knot_9_visited)}")
