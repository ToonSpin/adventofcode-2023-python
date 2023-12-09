import math
import sys

def possibilities(time, distance):
    spread_squared = time * time - 4 * distance
    half_spread = .5 * math.sqrt(spread_squared)
    min_time_holding = math.floor(.5 * time - half_spread)
    max_time_holding = math.ceil(.5 * time + half_spread)
    return max_time_holding - min_time_holding - 1

input = sys.stdin.read()

lines = input.splitlines()

times = map(int, lines[0].split()[1:])
distances = map(int, lines[1].split()[1:])

races = zip(times, distances)

product = 1
for time, distance in races:
    product *= possibilities(time, distance)

print(f'The product of the ways you can win the races: {product}')

time_part_two = int(''.join(lines[0].split()[1:]))
distance_part_two = int(''.join(lines[1].split()[1:]))

num_possible = possibilities(time_part_two, distance_part_two)
print(f'The product for the single, longer race: {num_possible}')
