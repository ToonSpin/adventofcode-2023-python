import sys

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

grid = sys.stdin.read().splitlines()

def get_neighbors(x, y, max_y):
    neighbors = [(x+1, y, EAST), (x-1, y, WEST)]
    if y > 0:
        neighbors.append((x, y-1, NORTH))
    if y < max_y:
        neighbors.append((x, y+1, SOUTH))
    return neighbors

def get_nodes(grid):
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c != '#':
                if y == 0 or y == len(grid) - 1:
                    yield (x, y)
                    continue
                count = 0
                for p, q, _ in get_neighbors(x, y, len(grid) - 1):
                    if grid[q][p] != '#':
                        count += 1
                        if count > 2:
                            yield (x, y)
                            break

graph_part_one = {}
graph_part_two = {}
nodes = set(get_nodes(grid))
start = None
for x, y in nodes:
    graph_part_one[(x, y)] = []
    graph_part_two[(x, y)] = []
    if y == 0:
        start = (x, y, 0)
    for p, q, d in get_neighbors(x, y, len(grid) - 1):
        if grid[q][p] == '#':
            continue
        prev = (x, y)
        cost = 0
        part_two = False
        while True:
            cost += 1
            cell = grid[q][p]
            if cell == 'v' and d == NORTH:
                part_two = True
            if cell == '<' and d == EAST:
                part_two = True
            if cell == '^' and d == SOUTH:
                part_two = True
            if cell == '>' and d == WEST:
                part_two = True
            if (p, q) in nodes:
                graph_part_two[(x, y)].append((p, q, cost))
                if not part_two:
                    graph_part_one[(x, y)].append((p, q, cost))
                break
            neighbors = get_neighbors(p, q, len(grid) - 1)
            for pp, qq, dd in get_neighbors(p, q, len(grid) - 1):
                if grid[qq][pp] == '#':
                    continue
                if (pp, qq) == prev:
                    continue
                prev = (p, q)
                p = pp
                q = qq
                d = dd
                break

def get_longest_path(grid, graph, start, indices):
    x, y, cost = start
    max_y = len(grid) - 1
    queue = [(x, y, cost, 0)]
    lengths = []
    try:
        while True:
            x, y, cost, visited = queue.pop()
            visited |= 1 << indices[(x, y)]
            if y == max_y:
                lengths.append(cost)
                continue
            for p, q, c in graph[(x, y)]:
                if visited & (1 << indices[(p, q)]) > 0:
                    continue
                queue.append((p, q, cost + c, visited))
    except IndexError:
        pass
    return max(lengths)

indices = {node: i for i, node in enumerate(nodes)}
longest_path = get_longest_path(grid, graph_part_one, start, indices)
print(f'The longest path from start to end: {longest_path}')
longest_path = get_longest_path(grid, graph_part_two, start, indices)
print(f'The longest path from start to end, without slopes: {longest_path}')
