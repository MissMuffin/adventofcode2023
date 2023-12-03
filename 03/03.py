import operator
import functools
import collections
import string
import re

symbols = string.punctuation.replace('.', '')

with open("input.txt") as input_file:
    lines = [line.strip() for line in input_file]

gears = collections.defaultdict(set)

# part must have at least one symbol adjacent to it
def analyze_number(row, start, end, part_number):
    found_symbol = False

    # is previous char in row symbol
    if start - 1 >= 0 and lines[row][start - 1] in symbols:
        found_symbol = True
        if lines[row][start - 1] == '*': gears[(row, start - 1)].add(part_number)
    
    # is next char in row symbol
    if end < len(lines[row]) and lines[row][end] in symbols:
        found_symbol = True
        if lines[row][end] == '*': gears[(row, end)].add(part_number)
    
    # check adjacent chars in previous and next row if symbol
    for x in range(start - 1, end + 1):
        if x < 0 or x >= len(lines[row]):
            continue

        if row - 1 > 0 and lines[row - 1][x] in symbols:
            found_symbol = True
            if lines[row -1][x] == '*': gears[(row - 1, x)].add(part_number)

        if row + 1 < len(lines[row]) and lines[row + 1][x] in symbols:
            found_symbol = True
            if lines[row + 1][x] == '*': gears[(row + 1, x)].add(part_number)

    return found_symbol

part_numbers_sum = 0
gear_ratios = 0

for row, line in enumerate(lines):
    for match in re.finditer(r"\d+", line):

        start, end = match.span()
        number = int(match.group())

        is_part_number = analyze_number(row, start, end, number)

        if is_part_number:
            part_numbers_sum += number

for coord, parts in gears.items():
    if len(parts) == 2:
        gear_ratios += functools.reduce(operator.mul, parts)

print(part_numbers_sum)            
print(gear_ratios)            

