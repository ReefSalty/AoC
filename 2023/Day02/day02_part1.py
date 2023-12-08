# Define a function to check if the conditions are met for a given draw subset
def is_valid_draw(draw):
    red_count = sum(int(count.split()[0]) for count in draw if count.split()[1] == 'red')
    green_count = sum(int(count.split()[0]) for count in draw if count.split()[1] == 'green')
    blue_count = sum(int(count.split()[0]) for count in draw if count.split()[1] == 'blue')

    return red_count <= 12 and green_count <= 13 and blue_count <= 14

# Read lines from the file
lines = open("2023/Day02/puzzle_input.txt", "r").readlines()

# Calculate the sum of IDs for valid games
sum_of_ids = 0

for line in lines:
    # Extract the draw subsets from the line
    draw_subsets = [subset.split(', ') for subset in line.split(':')[1].strip().split(';')]

    # Check if all draw subsets meet the conditions
    if all(is_valid_draw(draw) for draw in draw_subsets):
        sum_of_ids += int(line.split(':')[0].split()[1])

# Print the result
print("Sum of IDs of possible games:", sum_of_ids)
