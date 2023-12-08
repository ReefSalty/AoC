total = 0
with open('2023/Day01/input_text.txt') as f:
   for line in f:
    n =''.join(i for i in line if i.isdigit())
    first_digit = str(n[0])
    last_digit = str(n[-1])
    sum = first_digit + last_digit
    sum = int(sum)
    total = total + sum
print(total)
