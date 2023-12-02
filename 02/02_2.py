import operator
import functools
import collections

with open("input.txt") as input_file:
    lines = [line.split(':')[-1].strip() for line in input_file]

powers = []

for i, game in enumerate(lines):

    highest = collections.defaultdict(lambda: -1)

    for r in game.split(';'):

        for s in r.split(','):
            n = int(s.split()[0].strip())
            c = s.split()[1].strip()

            # print(n, c)

            if highest[c] < n:
                highest[c] = n

    powers.append(functools.reduce(operator.mul, highest.values(), 1))    

# print(powers)

result_1 = sum(powers)
print(result_1)
    