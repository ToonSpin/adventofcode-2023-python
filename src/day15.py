import sys

input = sys.stdin.read().strip().split(',')

def hash(s):
    result = 0
    for c in s:
        result += ord(c)
        result *= 17
        result %= 256
    return result

class BoxArray:
    def __init__(self):
        self.boxes = [[] for _ in range(256)]
        self.focal_lengths = {}

    def remove_lens(self, label):
        box = hash(label)
        try:
            self.boxes[box].remove(label)
        except ValueError:
            pass

    def update_lens(self, label, focal_length):
        box = hash(label)
        try:
            i = self.boxes[box].index(label)
            self.boxes[box][i] = label
        except ValueError:
            self.boxes[box].append(label)
        finally:
            self.focal_lengths[label] = focal_length

    def process_step(self, step):
        if step[-1] == '-':
            op = '-'
            label = step[:-1]
            self.remove_lens(label)
        else:
            label, focal_length = step.split('=')
            focal_length = int(focal_length)
            self.update_lens(label, focal_length)

    def focusing_power(self):
        total = 0
        for box_id, b in enumerate(self.boxes):
            for slot_id, label in enumerate(b):
                total += (box_id + 1) * (slot_id + 1) * self.focal_lengths[label]
        return total

part_one = sum(map(hash, input))
print(f'The sum of HASH results of all the steps: {part_one}')

a = BoxArray()
for step in input:
    a.process_step(step)

print(f'The total focusing power of the lenses: {a.focusing_power()}')
