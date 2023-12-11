import sys

class Grid:
    def __init__(self, lines):
        self.lines = lines
        self.empty_rows = Grid._get_empty_rows(lines)
        self.empty_columns = Grid._get_empty_columns(lines)

        galaxies = []
        for y, line in enumerate(lines):
            galaxies += [(x, y) for (x, c) in enumerate(line) if c == '#']
        self.galaxies = galaxies

    def total_intergalactic_distance(self, factor):
        d = 0
        for i in range(len(self.galaxies)):
            for j in range(i+1, len(self.galaxies)):
                d += self.distance_between_galaxies(i, j, factor)
        return d

    def distance_between_galaxies(self, i, j, factor):
        a, b = self.galaxies[i], self.galaxies[j]
        x1, x2 = min(a[0], b[0]), max(a[0], b[0])
        y1, y2 = min(a[1], b[1]), max(a[1], b[1])
        columns = [c for c in self.empty_columns if c >= x1 and c < x2]
        rows = [r for r in self.empty_rows if r >= y1 and r < y2]
        return x2 + y2 - x1 - y1 + (factor - 1) * (len(columns) + len(rows))

    @staticmethod
    def _get_empty_rows(lines):
        result = []
        for i, line in enumerate(lines):
            if all([c == '.' for c in line]):
                result.append(i)
        return result

    @staticmethod
    def _get_empty_columns(lines):
        result = []
        for i in range(len(lines[0])):
            if all([c == '.' for c in [line[i] for line in lines]]):
                result.append(i)
        return result

lines = sys.stdin.read().splitlines()
grid = Grid(lines)

distance_part_one = grid.total_intergalactic_distance(2)
print(f'The sum of lengths with the younger galaxies: {distance_part_one}')

distance_part_two = grid.total_intergalactic_distance(1000000)
print(f'The sum of lengths with the older galaxies: {distance_part_two}')
