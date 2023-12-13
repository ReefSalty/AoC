def extract_numbers(input_string):
    number_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    numbers = [number_dict[word] if word in number_dict else word for word in input_string.split() if word in number_dict or word.isdigit()]

    return ''.join(numbers)

total = 0
with open('2023/Day01/input_text.txt') as f:
   for line in f:
    n = extract_numbers(line)
    first_digit = str(n[0])
    last_digit = str(n[-1])
    sum = int(first_digit + last_digit)
    total = total + sum
print(total)