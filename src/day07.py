from copy import deepcopy
import sys

class Hand:
    from_part_one = '23456789TJQKA'
    from_part_two = 'J23456789TQKA'
    to_str = 'ABCDEFGHIJKLM'
    mapping_part_one = dict(zip(list(from_part_one), list(to_str)))
    mapping_part_two = dict(zip(list(from_part_two), list(to_str)))

    def __init__(self, cards):
        self.cards = cards

    def _cards_for_sort_key(self, part_two=False):
        if part_two:
            return [self.mapping_part_two[c] for c in self.cards]
        return [self.mapping_part_one[c] for c in self.cards]

    def sort_key(self, part_two=False):
        return [self.get_type(part_two)] + self._cards_for_sort_key(part_two)

    @staticmethod
    def permute_counts(counts):
        if sum(counts.values()) >= 5:
            yield counts
            return
        
        for card, count in counts.items():
            new_counts = deepcopy(counts)
            new_counts[card] = count + 1

            for c in Hand.permute_counts(new_counts):
                yield c

    @staticmethod
    def get_type_from_counts(counts, part_two=False):
        if part_two:
            if 'J' not in counts:
                return Hand.get_type_from_counts(counts, False)
            else:
                del counts['J']
                if len(counts) == 0: # Five jokers: five of a kind
                    return 6
                return max([Hand.get_type_from_counts(c, False) for c in Hand.permute_counts(counts)])

        max_count = 0
        for _, count in counts.items():
            if count > max_count:
                max_count = count

        if max_count == 5:
            return 6
        if max_count == 4:
            return 5
        if max_count == 3:
            if len(counts) == 2:
                return 4
            return 3
        if max_count == 2:
            if len(counts) == 3:
                return 2
            return 1
        return 0

    def get_type(self, part_two=False):
        counts = {}
        for c in self.cards:
            counts[c] = counts[c] + 1 if c in counts else 1
        return Hand.get_type_from_counts(counts, part_two)

input = []
for line in sys.stdin.read().splitlines():
    cards, rank = line.split()
    input.append((Hand(cards), int(rank)))

def winnings(input, part_two=False):
    ranked = zip(range(1, len(input) + 1), sorted(input, key=lambda t: t[0].sort_key(part_two)))

    total = 0
    for rank, (_, bid) in ranked:
        total += rank * bid

    return total

print(f'The total winnings are: {winnings(input)}')
print(f'The total winnings using the new joker rule are: {winnings(input, True)}')
