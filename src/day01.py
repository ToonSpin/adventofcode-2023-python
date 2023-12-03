import sys

symbols_part_one = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_part_two = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

symbols_part_one = dict(zip(symbols_part_one, range(1,1000)))
symbols_part_two = dict(zip(symbols_part_two, range(1,1000)))
symbols_part_two |= symbols_part_one

def first_and_last_as_int(text, symbols):
    first = (1000, 'dummy')
    last = (-1, 'dummy')

    for symbol in symbols:
        pos = text.find(symbol)
        if pos >= 0:
            first = min(first, (pos, symbol))

        pos = text.rfind(symbol)
        if pos >= 0:
            last = max(last, (pos, symbol))

    return symbols[first[1]] * 10 + symbols[last[1]]

input = sys.stdin.read()

sum = 0
for line in input.splitlines():
    sum += first_and_last_as_int(line, symbols_part_one)
print(f'The sum of the calibration values: {sum}')

sum = 0
for line in input.splitlines():
    sum += first_and_last_as_int(line, symbols_part_two)
print(f'The sum including spelled out digits: {sum}')
