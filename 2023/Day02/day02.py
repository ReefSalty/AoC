# read input file and create list of input lines
file = open("2023/Day02/puzzle_input.txt", "r")
input = file.read()
input_list = input.split('\n')

# part 1
sum = 0
for ind, inp in enumerate(input_list):
    inp = inp.split(':')[1].split(';')
    possible = True
    for games in inp:
        games = games.strip().split(',')

        for game in games:
            game = game.strip().split(' ')
            if ((game[1] == 'red' and int(game[0]) > 12) or
                (game[1] == 'green' and int(game[0]) > 13) or
                (game[1] == 'blue' and int(game[0]) > 14)):
                possible = False
    if possible:
        sum += (ind+1)
print(sum)

# part 2
sum = 0
for inp in input_list:
    inp = inp.split(':')[1].split(';')
    rgb = [0, 0, 0]
    for games in inp:
        games = games.strip().split(',')
        for game in games:
            game = game.strip().split(' ')
            if game[1] == 'green' and int(game[0]) > rgb[1]:
                rgb[1] = int(game[0])
            if game[1] == 'red' and int(game[0]) > rgb[0]:
                rgb[0] = int(game[0])
            if game[1] == 'blue' and int(game[0]) > rgb[2]:
                rgb[2] = int(game[0])
    
    sum += (rgb[0]*rgb[1]*rgb[2])
print(sum)