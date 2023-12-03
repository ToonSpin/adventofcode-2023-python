import sys

class Sample:
    def __repr__(self):
        return f'{self.red}R {self.green}G {self.blue}B'

    def __init__(self, s):
        self.red = 0
        self.green = 0
        self.blue = 0
        for description in s.split(', '):
            if description.endswith(' red'):
                self.red += int(description[:-4])
            if description.endswith(' green'):
                self.green += int(description[:-6])
            if description.endswith(' blue'):
                self.blue += int(description[:-5])

    def possible(self):
        return self.red <= 12 and self.green <= 13 and self.blue <= 14

    def power(self):
        return self.red * self.green * self.blue

    def combine(self, other):
        other.red = max(self.red, other.red)
        other.green = max(self.green, other.green)
        other.blue = max(self.blue, other.blue)
        return other

class Game:
    def __repr__(self):
        samples = ', '.join([str(sample) for sample in self.samples])
        return f'G{self.id}: {samples}'

    def __init__(self, s):
        game_description, samples_description = s.split(': ')
        self.id = int(game_description[5:])
        self.samples = [Sample(s) for s in samples_description.split('; ')]

    def possible(self):
        return all([sample.possible() for sample in self.samples])

    def minimum_power(self):
        minimum_set = Sample('')
        for sample in self.samples:
            minimum_set = minimum_set.combine(sample)
        return minimum_set.power()

input = sys.stdin.read()
games = [Game(line) for line in input.splitlines()]

sum_part_one = sum([g.id if g.possible() else 0 for g in games])
print(f'The product of IDs of possible games: {sum_part_one}')

sum_part_two = sum([g.minimum_power() for g in games])
print(f'The product of minimum powers: {sum_part_two}')
