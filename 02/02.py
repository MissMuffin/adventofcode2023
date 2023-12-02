with open("input.txt") as input_file:
    lines = [line.split(':')[-1].strip() for line in input_file]

red = 12
green = 13
blue = 14

valid_games = []

for i, game in enumerate(lines):

    is_valid = True

    for r in game.split(';'):

        t = 0

        for s in r.split(','):
            n = int(s.split()[0].strip())
            c = s.split()[1].strip()

            # print(n, c)

            t += int(n)

            if (c == 'green' and n > green) or (c == 'red' and n > red) or (c == 'blue' and n > blue): 
                is_valid = False
    

    if is_valid:
        valid_games.append(i)

# print(valid_games)

result_1 = sum(valid_games) + len(valid_games)
print(result_1)
    