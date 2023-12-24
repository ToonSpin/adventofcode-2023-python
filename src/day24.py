import sys


TEST_AREA_MIN = 200000000000000
TEST_AREA_MAX = 400000000000000


class Hailstone:
    def __init__(self, line):
        pos, vel = line.split(' @ ')
        x, y, z = pos.split(', ')
        u, v, w = vel.split(', ')
        self.pos = (int(x), int(y), int(z))
        self.vel = (int(u), int(v), int(w))

    def __repr__(self):
        x, y, z = self.pos
        u, v, w = self.vel
        return f'{x}, {y}, {z} @ {u}, {v}, {w}'

    def is_2d_parallel_to(self, other):
        p, q, _ = self.vel
        r, s, _ = other.vel
        return p * s == q * r

    def x_in_the_past(self, x):
        a, _, _ = self.pos
        p, _, _ = self.vel
        return x > a if p < 0 else x < a

    def point_of_intersection_2d(self, other):
        a, b, _ = self.pos
        p, q, _ = self.vel
        c, d, _ = other.pos
        r, s, _ = other.vel
        x = (b * p * r + c * p * s - a * q * r - d * p * r) / (p * s - q * r)
        y = (q / p) * (x - a) + b
        return (x, y)

    def future_2d_intersection(self, other):
        if self.is_2d_parallel_to(other):
            return None
        x, y = self.point_of_intersection_2d(other)
        if self.x_in_the_past(x):
            return None
        if other.x_in_the_past(x):
            return None
        return (x, y)


input = [Hailstone(line) for line in sys.stdin.read().splitlines()]

hailstone_count = len(input)
count = 0
for i in range(hailstone_count):
    for j in range(i+1,hailstone_count):
        p = input[i].future_2d_intersection(input[j])
        if p is None:
            continue
        x, y = p
        if x < TEST_AREA_MIN or x > TEST_AREA_MAX:
            continue
        if y < TEST_AREA_MIN or y > TEST_AREA_MAX:
            continue
        count += 1

print(f'The number of intersections inside the test area: {count}')
