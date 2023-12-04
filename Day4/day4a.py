import re

total = 0
with open('./input.txt', 'r') as f:
    cards = f.read().splitlines()
for card in cards:
    numbers = [int(x) for x in re.findall(r'\d+', card)]
    nums = {}
    for i in numbers[1:11]:
        nums[i] = 0
    for i in numbers[11:]:
        if nums.get(i) is not None:
            nums[i] += 1
    wins = 0
    for k, v in nums.items():
        wins += v
    if wins > 0:
        total += 2**(wins-1)
print(total)
