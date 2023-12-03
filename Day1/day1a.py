import re

sum = 0
with open('./input.txt','r') as f:
    for foo in f:
        bar = re.findall(r'\d', foo)
        sum += int(bar[0]+bar[-1])
print(sum)
