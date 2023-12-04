import re

total = 0
with open('./input.txt', 'r') as f:
    cards = f.read().splitlines()
copies = [1] * len(cards)
for card in cards:
    numbers = [int(x) for x in re.findall(r'\d+', card)]
    nums = {}
    curr = numbers[0]
    for i in numbers[1:11]:
        nums[i] = 0
    for i in numbers[11:]:
        if nums.get(i) is not None:
            nums[i] += 1
    wins = 0
    for k, v in nums.items():
        wins += v
    if wins > 0:
        for i in range(curr, curr + wins):
            copies[i] += copies[curr-1]
print(sum(copies))
