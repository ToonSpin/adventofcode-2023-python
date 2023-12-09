import re
import sys

input = sys.stdin.read()

class Range:
    def __init__(self, fr, size):
        self.lower = fr
        self.upper = fr + size

    def __repr__(self):
        return f'[{self.lower}, {self.upper})'

    def __hash__(self):
        return hash((self.lower, self.upper))

    def __eq__(self, other):
        return self.lower == other.lower and self.upper == other.upper

    def is_disjoint_with(self, other: 'Range'):
        if self.upper <= other.lower:
            return True
        if other.upper <= self.lower:
            return True
        return False

    def intersects(self, other: 'Range'):
        return not self.is_disjoint_with(other)

    def contains(self, n: int) -> bool:
        return n >= self.lower and n < self.upper

    @staticmethod
    def split_range_lists(l1, l2):
        result = l2
        for r1 in l1:
            new = []
            for r2 in result:
                new += r1.split(r2)
            result = list(set(new))
        return result

    def split(self, other: 'Range'):
        if self.is_disjoint_with(other):
            return [self, other]
        bounds = [
            self.lower,
            self.upper,
            other.lower,
            other.upper,
        ]
        bounds.sort()
        ranges = []
        for n in range(1, 4):
            size = bounds[n] - bounds[n-1]
            if size > 0:
                ranges.append(Range(bounds[n-1], size))
        return ranges

class Map:
    def __init__(self, block):
        block = block.splitlines()
        regex = re.compile('([a-z]+)-to-([a-z]+) map:')
        matches = regex.match(block[0])
        self.map_from = matches.group(1)
        self.map_to = matches.group(2)
        self.maps = []
        for line in block[1:]:
            if len(line) > 0:
                to, fr, size = tuple(map(int, line.split()))
                self.maps.append((Range(fr, size), to))

    def map(self, n):
        for range, to in self.maps:
            if range.contains(n):
                return n - range.lower + to
        return n

    def map_range(self, r):
        to_map = [r]
        for range in self.get_ranges():
            if any([range.intersects(r) for r in to_map]):
                to_map = Range.split_range_lists(to_map, [range])
        to_map = [range for range in to_map if range.intersects(r)]
        result = [Range(self.map(r.lower), r.upper - r.lower) for r in to_map]
        return result

    def get_from(self):
        return self.map_from

    def get_to(self):
        return self.map_to

    def get_ranges(self):
        return [r for (r, _) in self.maps]

blocks = input.split('\n\n')
seeds = list(map(int, blocks[0].split(': ')[1].split()))

maps = {}

for m in map(Map, blocks[1:]):
    maps[m.get_from()] = m

def get_location_for_seed(s):
    type = 'seed'
    value = s
    while type != 'location':
        m = maps[type]
        value = m.map(value)
        type = m.get_to()
    return value

def get_location_for_range(range):
    type = 'seed'
    ranges = [range]
    while type != 'location':
        m = maps[type]
        mapped = []
        for r in ranges:
            mapped += m.map_range(r)
        ranges = list(set(mapped))
        type = m.get_to()
    return min([r.lower for r in ranges])

loc_part_one = min([get_location_for_seed(s) for s in seeds])
print(f'The lowest location number for the seeds: {loc_part_one}')

ranges = [Range(seeds[n], seeds[n+1]) for n in range(0, len(seeds), 2)]

loc_part_two = min([get_location_for_range(r) for r in ranges])
print(f'The lowest location number for the ranges: {loc_part_two}')
