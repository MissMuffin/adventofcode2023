numbers = [x for x in '123456789']

numbers_str = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

with open("input.txt") as input_file:
    lines = [line.strip() for line in input_file]

def getNumber(line):
    return int([char for char in line if char in numbers][0] + [char for char in line[::-1] if char in numbers][0])

result_1 = sum([getNumber(line) for line in lines])
print(result_1)

def repl_num_str(line):
    for key, val in numbers_str.items():
        line = line.replace(key, val)
    return line

result_2 = sum([getNumber(repl_num_str(line)) for line in lines])
print(result_2)