import re

total = 0
symbols = ['+', '-', '!', '@', '#', '$', '%', '&', '*', '/', '=']
with open('./input.txt', 'r') as f:
    schematic = f.read().splitlines()
    row_count = len(schematic)
    col_count = len(schematic[0])
    curr_row = 0
    for row in schematic:
        matches = re.finditer(r'\d+', row)  # match object for each digit series in row
        # for each match object, check if it's valid
        for match in matches:
            isPart = False
            partNum = int(match[0])
            a, b = match.span()
            a = max(0, a-1)
            b = min(b, col_count-1)
            if row[a] in symbols or row[b] in symbols:
                total += partNum
                continue
            if curr_row > 0:
                if any([x in symbols for x in schematic[curr_row-1][a:b+1]]):
                    total += partNum
                    continue
            if curr_row < row_count-1:
                if any([x in symbols for x in schematic[curr_row+1][a:b+1]]):
                    total += partNum
        curr_row += 1  # increment row
print(total)
