total = 0
with open('/workspaces/AoC/2023/Day 1/aoc1.txt') as f:
   for line in f:
    n =''.join(i for i in line if i.isdigit())
    first_digit = str(n[0])
    last_digit = str(n[-1])
    sum = first_digit + last_digit
    sum = int(sum)
    total = total + sum
print(total)
