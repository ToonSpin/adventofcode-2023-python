import math
import sys

input = sys.stdin.read()
lines = input.splitlines()

instructions = lines[0]
nodes = {}

for line in lines[2:]:
    node = line[0:3]
    left = line[7:10]
    right = line[12:15]
    nodes[node] = (left, right)

def count_steps_part_one(nodes, instructions):
    count = 0
    node = 'AAA'
    while node != 'ZZZ':
        left, right = nodes[node]
        instruction = instructions[count % len(instructions)]
        node = left if instruction == 'L' else right
        count += 1
    return count

def count_steps_part_two(nodes, instructions):
    count = 0
    positions = [node for node in nodes if node[2] == 'A']
    found = {node: 0 for node in nodes if node[2] == 'Z'}
    num_found = 0
    while True:
        if num_found == len(found):
            break
        for i, node in enumerate(positions):
            left, right = nodes[node]
            instruction = instructions[count % len(instructions)]
            node = left if instruction == 'L' else right
            positions[i] = node
            if node[2] == 'Z' and found[node] == 0:
                found[node] = count
                num_found += 1
        count += 1
    result = 1
    for n in found.values():
        result = math.lcm(result, n + 1)
    return result

print(count_steps_part_one(nodes, instructions))
print(count_steps_part_two(nodes, instructions))
