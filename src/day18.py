import sys

directions = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}

def input_to_vertices(input):
    x, y = (0, 0)
    result = []
    for direction, dist in input:
        if direction == 'R':
            x += dist
        elif direction == 'D':
            y += dist
        elif direction == 'L':
            x -= dist
        elif direction == 'U':
            y -= dist
        result.append((x, y))
    return result
        
def vertices_to_area(vertices):
    total = 0
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        x1, y1 = vertices[i]
        x2, y2 = vertices[j]
        total += x1 * y2
        total -= x2 * y1
        total += abs(x1 - x2)
        total += abs(y1 - y2)
    return total // 2 + 1

input_part_one = []
input_part_two = []
for line in sys.stdin.read().splitlines():
    dir_part_one, dist_part_one, color = line.split(' ')
    color = color[2:-1]
    input_part_one.append((dir_part_one, int(dist_part_one)))

    dist_part_two = int(color[:5], 16)
    dir_part_two = directions[color[5:]]
    input_part_two.append((dir_part_two, dist_part_two))

area_part_one = vertices_to_area(input_to_vertices(input_part_one))
print(f'The volume of the smaller lagoon: {area_part_one}')

area_part_two = vertices_to_area(input_to_vertices(input_part_two))
print(f'The volume of the larger lagoon: {area_part_two}')
