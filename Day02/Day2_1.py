red_cubes_count = 12
green_cubes_count = 13
blue_cubes_count = 14

inventory = {
    "red": red_cubes_count,
    "green": green_cubes_count,
    "blue": blue_cubes_count
}

cumulative_impossible_game_indices = 0

fname = "./Day02/Day2_1.txt"
# fname = "./Day02/example.txt"
with open(fname) as f:
    for game in f.readlines():

        game_is_possible = True

        game = game.rstrip()
        print("----------------")
        print(game)

        # Get the index of the game
        game_index = int(game.split(": ")[0].replace("Game ",""))
        print(game_index)

        # Get the data from each round of the game
        game_data = game.split(": ")[1]
        rounds  = game_data.split("; ")
        for round in rounds: 
            print(round)
            colored_cube_group = round.split(", ")
            for group in colored_cube_group:
                count = int(group.split(" ")[0])
                color = group.split(" ")[1]
                if count > inventory[color]:
                    game_is_possible = False

        if game_is_possible:
            cumulative_impossible_game_indices += game_index

print("----------------")
print(f"Answer: {cumulative_impossible_game_indices}")
# Answer: 2169
                