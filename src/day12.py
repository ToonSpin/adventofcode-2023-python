import cProfile
import sys

class SpringRecord:
    def __init__(self, line):
        self.record, groups = line.split(' ')
        self.groups = list(map(int, groups.split(',')))
    
    def __repr__(self):
        groups = ','.join(map(str, self.groups))
        return f'{self.record} {groups}'

    def part_two(self, factor=5):
        new_record = '?'.join(factor * [self.record])
        groups = ','.join(map(str, self.groups))
        new_groups = ','.join(factor * [groups])
        return SpringRecord(f'{new_record} {new_groups}')

    def _match(self, gaps):
        i = 0
        for gap, group in zip(gaps, self.groups):
            while gap > 0:
                c = self.record[i] 
                if c != '?' and c != '.':
                    return False
                gap -= 1
                i += 1
            while group > 0:
                c = self.record[i] 
                if c != '?' and c != '#':
                    return False
                group -= 1
                i += 1
        for c in self.record[i:]:
            if c == '#':
                return False
        return True

    def num_possibilities(self, gaps = []):
        if len(gaps) == len(self.groups):
            if self._match(gaps):
                return 1
            return 0

        headroom = len(self.record) - sum(gaps) - sum(self.groups)
        if headroom == 0:
            return 0

        count = 0
        if len(gaps) == 0:
            start = 0
        else:
            start = 1

        for l in range(start, headroom + 1):
            count += self.num_possibilities(gaps + [l])

        return count
    
input = [SpringRecord(line) for line in sys.stdin.read().splitlines()]

num_possibilities = sum(record.num_possibilities() for record in input)
print(num_possibilities)

input = [record.part_two(3) for record in input]
cProfile.run('num_possibilities = sum(record.num_possibilities() for record in input)')
print(num_possibilities)
