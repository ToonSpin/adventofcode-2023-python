import re
import sys

input = sys.stdin.read()

class Map:
    def __init__(self, block):
        block = block.split('\n')
        regex = re.compile('([a-z]+)-to-([a-z]+) map:')
        matches = regex.match(block[0])
        self.map_from = matches.group(1)
        self.map_to = matches.group(2)
        self.maps = []
        for line in block[1:]:
            if len(line) > 0:
                self.maps.append(tuple(map(int, line.split())))
    
    def map(self, n):
        for to, fr, size in self.maps:
            if n >= fr and n - fr < size:
                return n - fr + to
        return n

    def get_from(self):
        return self.map_from

    def get_to(self):
        return self.map_to

blocks = input.split('\n\n')
seeds = map(int, blocks[0].split(': ')[1].split())
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

print(min([get_location_for_seed(s) for s in seeds]))
