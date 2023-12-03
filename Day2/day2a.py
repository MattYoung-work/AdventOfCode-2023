import re


def max_cubes(line):
    a = {'r': 0, 'b': 0, 'g': 0}
    cubes = re.findall(r'(\d+) (\w)', line)  # get number and color of each cube set
    for n, c in cubes:
        a[c] = max(int(n), a[c])  # get max of each color
    return a


max_dice = {'r': 12, 'g': 13, 'b': 14}

total = 0
with open('./input.txt', 'r') as f:
    for line in f:
        foo = max_cubes(line)
        game = int(re.findall(r'Game (\d+)', line)[0])
        total += game * all([n <= max_dice[c] for c, n in foo.items()])
print(total)
