import sys

class ReflectorDish:
    def __init__(self, lines):
        self.lines = lines

    def __str__(self):
        return '\n'.join(self.lines)

    def move_rocks_west(self):
        new_lines = []
        for line in self.lines:
            new_line = ''
            for segment in line.split('#'):
                count = 0
                for c in segment:
                    if c == 'O':
                        count += 1
                new_line += count * 'O' + (len(segment) - count) * '.' + '#'
            new_lines.append(new_line[:-1])
        self.lines = new_lines

    def rotate_cw(self):
        new_lines = ['' for _ in range(len(self.lines))]
        for line in self.lines:
            for c, tile in enumerate(line):
                new_lines[c] = tile + new_lines[c]
        self.lines = new_lines

    def rotate_ccw(self):
        new_lines = ['' for _ in range(len(self.lines))]
        for line in self.lines:
            for c, tile in enumerate(line):
                new_lines[c] = new_lines[c] + tile
        self.lines = list(reversed(new_lines))

    def load(self):
        total = 0
        for i, line in enumerate(self.lines):
            factor = len(self.lines) - i
            total += factor * len(list(filter(lambda c: c == 'O', line)))
        return total

    def cycle(self):
        self.rotate_ccw()
        for _ in range(4):
            self.move_rocks_west()
            self.rotate_cw()
        self.rotate_cw()

input = sys.stdin.read()

part_one = ReflectorDish(input.splitlines())
part_one.rotate_ccw()
part_one.move_rocks_west()
part_one.rotate_cw()
print(f'The total load on the north beam after one tilt: {part_one.load()}')

part_two = ReflectorDish(input.splitlines())
dishes_seen = {}
cycle_length = None
i = 0
while i < 1000000000:
    part_two.cycle()
    dish = str(part_two)
    if cycle_length is None and dish in dishes_seen:
        cycle_length = i - dishes_seen[dish]
        span = 1000000000 - i
        num_cycles_elapsed = span // cycle_length
        i += cycle_length * num_cycles_elapsed
    dishes_seen[dish] = i
    i += 1
print(f'The load after 1000000000 cycles: {part_two.load()}')
