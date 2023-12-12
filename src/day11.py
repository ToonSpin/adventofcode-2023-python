import sys

class Grid:
    def __init__(self, lines):
        self.lines = lines
        self.empty_rows = Grid._get_empty_rows(lines)
        self.empty_columns = Grid._get_empty_columns(lines)

        self._empty_cols_between = {}
        self._empty_rows_between = {}

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

    def empty_rows_between(self, y1, y2):
        if (y1, y2) not in self._empty_rows_between:
            a, b = min(y1, y2), max(y1, y2)
            rows = [c for c in self.empty_rows if c >= a and c < b]
            self._empty_rows_between[(y1, y2)] = len(rows)
            self._empty_rows_between[(y2, y1)] = len(rows)
        return self._empty_rows_between[(y1, y2)]

    def empty_cols_between(self, x1, x2):
        if (x1, x2) not in self._empty_cols_between:
            a, b = min(x1, x2), max(x1, x2)
            columns = [c for c in self.empty_columns if c >= a and c < b]
            self._empty_cols_between[(x1, x2)] = len(columns)
            self._empty_cols_between[(x2, x1)] = len(columns)
        return self._empty_cols_between[(x1, x2)]

    def distance_between_galaxies(self, i, j, factor):
        (x1, y1), (x2, y2) = self.galaxies[i], self.galaxies[j]
        columns = self.empty_cols_between(x1, x2)
        rows = self.empty_rows_between(y1, y2)
        return abs(x2 - x1) + abs(y2 - y1) + (factor - 1) * (columns + rows)

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
