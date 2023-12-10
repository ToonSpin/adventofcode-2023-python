import math
import re
import sys

class Grid:
    possible_pipes = {
        (0, -1): '|7FS',
        (1, 0):  '-J7S',
        (0, 1):  '|LJS',
        (-1, 0): '-LFS',
    }

    possible_dirs = {
        'S': [(0, -1),(1, 0),(0, 1),(-1, 0),],
        '|': [(0, -1),(0, 1),],
        '-': [(1, 0),(-1, 0),],
        'L': [(0, -1),(1, 0),],
        'J': [(0, -1),(-1, 0),],
        '7': [(0, 1),(-1, 0),],
        'F': [(1, 0),(0, 1),],
    }

    pipes_to_unicode = {
        'F': '\u250C\u2500',
        '7': '\u2510 ',
        'L': '\u2514\u2500',
        'J': '\u2518 ',
        '-': '\u2500\u2500',
        '|': '\u2502 ',
        '.': '  ',
        'S': '* ',
    }

    def __repr__(self):
        repr = []
        for row in self.grid:
            line = ''.join(row)
            for fr, to in self.pipes_to_unicode.items():
                line = line.replace(fr, to)
            repr.append(line)
        return '\n'.join(repr)

    def __init__(self, lines):
        self.grid = [list(line) for line in lines]
        start = (-1, -1)
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == 'S':
                    start = (x, y)
                    break
            if start != (-1, -1):
                break
        self.start = start

    def count_non_empty(self):
        count = 0
        for row in self.grid:
            count += len([cell for cell in row if cell != '.'])
        return count

    def count_interior(self):
        count = 0
        loop_re = re.compile('F-*7|L-*J')
        edge_re = re.compile('F-*J|L-*7')
        for row in self.grid:
            row = ''.join(row)
            row = loop_re.sub('', row)
            row = edge_re.sub('|', row)
            parity = 0
            for cell in row:
                if cell == '|':
                    parity += 1
                if cell == '.':
                    count += parity % 2
        return count

    def width(self):
        return len(self.grid[0])

    def height(self):
        return len(self.grid)

    def out_of_bounds(self, x, y):
        if x < 0 or x >= self.width():
            return True
        if y < 0 or y >= self.width():
            return True
        return False


    def interpolate_start(self, x, y):
        poss_at_start = []

        for (p, q), possible in self.possible_pipes.items():
            test_x = x + p
            test_y = y + q
            if self.out_of_bounds(test_x, test_y):
                continue
            if self.grid[test_y][test_x] in possible:
                poss_at_start.append((p, q))

        for tile, possible in self.possible_dirs.items():
            if tile == 'S':
                continue
            if poss_at_start[0] in possible and poss_at_start[1] in possible:
                self.grid[y][x] = tile
                break

    def only_loop(self):
        new_grid = [list(self.width() * '.') for y in range(self.height())]
        x, y = self.start
        prev_pos = (x, y)
        new_grid[y][x] = 'S'
        count = 1

        while count == 1 or self.grid[y][x] != 'S':
            new_x, new_y = self._next_in_loop(new_grid, (x, y), prev_pos)
            prev_pos = (x, y)
            (x, y) = (new_x, new_y)
            count += 1

        result = Grid(new_grid)
        result.interpolate_start(x, y)
        return result

    def _next_in_loop(self, new_grid, pos, prev_pos):
        x, y = pos
        cur_tile = self.grid[y][x]
        new_grid[y][x] = cur_tile

        done = False
        for (p, q) in self.possible_dirs[cur_tile]:
            if done:
                break
            new_x = x + p
            new_y = y + q

            if (new_x, new_y) == prev_pos:
                continue
            if self.out_of_bounds(new_x, new_y):
                continue

            for possible in self.possible_pipes[(p, q)]:
                if self.grid[new_y][new_x] in possible:
                    done = True
                    break

        return new_x, new_y

lines = sys.stdin.read().splitlines()
grid = Grid(lines)
only_loop = grid.only_loop()

max_distance = math.ceil(only_loop.count_non_empty() / 2)
print(f'The maximum distance from the starting position: {max_distance}')

interior = only_loop.count_interior()
print(f'The number of tiles the loop encloses: {interior}')
