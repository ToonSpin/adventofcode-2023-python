import functools
import sys

@functools.cache
def possibilities(record, groups):
    if len(groups) == 0:
        if any(c == '#' for c in record):
            return 0
        else:
            return 1
    first_group = groups[0]
    if len(record) < first_group:
        return 0

    if record[0] == '?':
        return possibilities('#' + record[1:], groups) + possibilities('.' + record[1:], groups)
    if record[0] == '.':
        return possibilities(record[1:], groups)
    
    if record[:first_group].replace('?', '#') != first_group * '#':
        return 0

    if record[first_group:first_group+1] == '#':
        return 0

    return possibilities(record[first_group+1:], groups[1:])

input = []
for line in sys.stdin.read().splitlines():
    record, groups = line.split(' ')
    groups = tuple(map(int, groups.split(',')))
    input.append((record, groups))

def part_two(record, groups, count=5):
    record = [record for _ in range(5)]
    record = '?'.join(record)
    return (record, tuple(count * list(groups)))

total = 0
for record, groups in input:
    total += possibilities(record, groups)
print(f'The number of arrangements possible that meet the criteria: {total}')

total = 0
for record, groups in input:
    r, g = part_two(record, groups, count=5)
    total += possibilities(r, g)
print(f'The number of possibilities after unfolding: {total}')
