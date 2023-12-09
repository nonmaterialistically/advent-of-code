import os
from collections import defaultdict
import re
import math

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open("input.txt", "r") as file:
    lines = file.readlines()

lr_instructions = [c for c in lines[0].strip()]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
tree = defaultdict(Node)

starts = []
for line in lines[2:]:
    match = re.match(r"(\w+)\s\=\s\((\w+)\,\s(\w+)\)", line)
    if match:
        node = match.group(1)
        left = match.group(2)
        right = match.group(3)
        #Get all the starts for part2
        if node[2] == "A":
            starts.append(node)
        #Build the tree for everthing
        if node not in tree:
            tree[node] = Node(node)
        if left not in tree:
            tree[left] = Node(left)
        if right not in tree:
            tree[right] = Node(right)
        tree[node].left = tree[left]
        tree[node].right = tree[right]

current_node = tree["AAA"]
i = 0
part1 = 0
while current_node.value != "ZZZ":
    part1 += 1
    instruction = lr_instructions[i]
    if instruction == "L":
        current_node = current_node.left
    elif instruction == "R":
        current_node = current_node.right
    if i == len(lr_instructions)-1:
        i = 0
    else:
        i += 1
print(f"Part 1: {part1}")

part2 = 0
current_nodes = [tree[start] for start in starts]
ghost_loop_counters = [0 for _ in range(len(current_nodes))]
i = 0
while not all([node.value.endswith("Z") for node in current_nodes]):
    instruction = lr_instructions[i]
    if instruction == "L":
        for k, node in enumerate(current_nodes):
            if not node.value.endswith("Z"):
                ghost_loop_counters[k] += 1
                current_nodes[k] = node.left
    elif instruction == "R":
        for k, node in enumerate(current_nodes):
            if not node.value.endswith("Z"):
                ghost_loop_counters[k] += 1
                current_nodes[k] = node.right
    if i == len(lr_instructions)-1:
        i = 0
    else:
        i += 1

part2 = math.lcm(*ghost_loop_counters)
print(f"Part 2: {part2}")