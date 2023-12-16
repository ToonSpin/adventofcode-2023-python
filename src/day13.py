import sys

class AxisNotFoundException(Exception):
    pass

class Pattern:
    def __init__(self, block):
        self.block = block.splitlines()
        self.block_flipped_h = Pattern._flip_h(self.block[:])
        self.block_flipped_v = Pattern._flip_v(self.block[:])

    @staticmethod
    def _find_h_axis(block_a, block_b, ignore_axis=-1):
        for offset in range(len(block_a) % 2, len(block_a) - 1, 2):
            if block_a[offset:] == block_b[:-offset]:
                axis = (len(block_a) - offset) // 2 + offset
                if ignore_axis != axis:
                    return axis
            if block_a[:-offset] == block_b[offset:]:
                axis = (len(block_a) - offset) // 2
                if ignore_axis != axis:
                    return axis
        raise AxisNotFoundException

    def find_h_axis(self, ignore_axis=-1):
        return Pattern._find_h_axis(self.block, self.block_flipped_v, ignore_axis)

    def find_v_axis(self, ignore_axis=-1):
        block_a = Pattern._transpose(self.block[:])
        block_b = Pattern._transpose(self.block_flipped_h)
        return Pattern._find_h_axis(block_a, block_b, ignore_axis)

    @staticmethod
    def _transpose(block):
        new_block = ['' for _ in range(len(block[0]))]
        for line in block:
            for (i, c) in enumerate(line):
                new_block[i] += c
        return new_block

    @staticmethod
    def _flip_h(block):
        new_block = []
        for line in block:
            new_block.append(''.join(reversed(line)))
        return new_block
    
    @staticmethod
    def _flip_v(block):
        block.reverse()
        return block

def get_block_score(block, ignore_score=-1):
    pattern = Pattern(block)
    try:
        if ignore_score > 0 and ignore_score < 100:
            axis = pattern.find_v_axis(ignore_score)
        else:
            axis = pattern.find_v_axis()
        return axis
    except AxisNotFoundException:
        if ignore_score >= 100:
            axis = pattern.find_h_axis(ignore_score / 100)
        else:
            axis = pattern.find_h_axis()
        return 100 * axis

blocks = sys.stdin.read().split('\n\n')
scores_part_one = []
for block in blocks:
    scores_part_one.append(get_block_score(block))
total_score = sum(scores_part_one)
print(f'The summary of all the notes on the patterns: {total_score}')

scores_part_two = []
for (i, block) in enumerate(blocks):
    for j, c in enumerate(block):
        new_block = None
        if c == '.':
            new_block = block[:j] + '#' + block[j+1:]
        if c == '#':
            new_block = block[:j] + '.' + block[j+1:]
        if new_block is None:
            continue

        try:
            score = get_block_score(new_block, scores_part_one[i])
            scores_part_two.append(score)
            break
        except AxisNotFoundException:
            pass

total_score = sum(scores_part_two)
print(f'The summary after unsmudging: {total_score}')
