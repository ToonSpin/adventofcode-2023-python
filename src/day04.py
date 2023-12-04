import sys

input = sys.stdin.read()

sum = 0
count = 0
num_winning = []
queue = []

for i, line in enumerate(input.splitlines()):
    _, numbers = line.split(':')
    winning, drawn = numbers.split('|')

    winning = filter(lambda s: len(s) > 0, winning.split(' '))
    drawn = filter(lambda s: len(s) > 0, drawn.split(' '))

    winning = set(map(int, winning))
    drawn = set(map(int, drawn))

    num_winning_found = len(drawn.intersection(winning))
    num_winning.append(num_winning_found)
    if num_winning_found > 0:
        sum += 2 ** (num_winning_found - 1)
    
    queue.append(i)

print(f'The total amount of points: {sum}')

memo_get_nonzero_won = {}
def get_nonzero_won(item):
    if item not in memo_get_nonzero_won:
        winning = num_winning[item]
        r = range(item + 1, item + winning + 1)
        memo_get_nonzero_won[item] = [n for n in r if num_winning[n] > 0]
    return memo_get_nonzero_won[item]

while len(queue) > 0:
    item = queue.pop()
    winning = num_winning[item]
    nonzero_won = get_nonzero_won(item)
    count += winning - len(nonzero_won) + 1
    queue += nonzero_won

print(f'The number of scratch cards you end up with: {count}')
