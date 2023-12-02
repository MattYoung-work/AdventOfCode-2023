import re

sum = 0
with open('./input.txt','r') as f:
    for foo in f:
        foo = foo.replace('one', 'o1e')
        foo = foo.replace('two', 't2o')
        foo = foo.replace('three', 't3e')
        foo = foo.replace('four', 'f4r')
        foo = foo.replace('five', 'f5e')
        foo = foo.replace('six', 's6x')
        foo = foo.replace('seven', 's7n')
        foo = foo.replace('eight', 'e8t')
        foo = foo.replace('nine', 'n9e')
        bar = re.findall(r'\d', foo)
        sum += int(bar[0]+bar[-1])
print(sum)