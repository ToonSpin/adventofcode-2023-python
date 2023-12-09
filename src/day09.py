import sys

lines = sys.stdin.read().splitlines()

histories = [list(map(int, l.split())) for l in lines]

def expand(history):
    histories = [history]
    last = history
    while not all(last[n - 1] == last[n] for n in range(1, len(last))):
        new = [last[n] - last[n - 1] for n in range(1, len(last))]
        histories.append(new)
        last = new
    return histories

def extrapolate(history):
    expanded = expand(history)
    expanded.reverse()
    extrapolated = []
    for i in range(len(expanded)):
        new = expanded[i]

        diff = 0 if i == 0 else expanded[i-1][-1]
        new.append(expanded[i][-1] + diff)

        diff = 0 if i == 0 else extrapolated[i-1][0]
        new = [expanded[i][0] - diff] + new

        extrapolated.append(new)
    extrapolated.reverse()
    return extrapolated

total_part_one = 0
total_part_two = 0

for h in histories:
    extrapolated = extrapolate(h)
    total_part_one += extrapolated[0][-1]
    total_part_two += extrapolated[0][0]

print(f'The sum of extrapolated next values: {total_part_one}')
print(f'The sum of extrapolated previous values: {total_part_two}')
