import re
import sys

class Engine:
    def __init__(self, lines):
        self.lines = lines
        self.dim = len(lines[0])
    
    def _get_symbol_locations(self):
        for y in range(self.dim):
            for x in range(self.dim):
                if self.lines[y][x] not in '0123456789.':
                    yield (x, y)

    def get_adjacent_numbers(self):
        regex = re.compile('\d+')
        for (x, y) in self._get_symbol_locations():
            symbol = self.lines[y][x]
            numbers = []
            for line in self.lines[y - 1:y + 2]:
                minx = x - 1
                maxx = x + 1

                while minx > 0 and line[minx] in '0123456789':
                    minx -= 1
                while maxx < self.dim - 1 and line[maxx] in '0123456789':
                    maxx += 1

                numbers += map(int, regex.findall(line[minx:maxx+1]))
            yield((symbol, numbers))

input = sys.stdin.read()
lines = input.splitlines()
engine = Engine(lines)

numbers = list(engine.get_adjacent_numbers())

sum_part_numbers = sum([sum(l) for (_, l) in numbers])
print(f'The sum of the part numbers: {sum_part_numbers}')

sum_gear_ratios = sum([l[0] * l[1] for (s, l) in numbers if s == '*' and len(l) == 2])
print(f'The sum of the gear ratios: {sum_gear_ratios}')