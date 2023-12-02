red_cubes_count = 12
green_cubes_count = 13
blue_cubes_count = 14

cumulative_game_power = 0

fname = "./Day02/Day2_1.txt"
# fname = "./Day02/example.txt"
with open(fname) as f:
    for game in f.readlines():

        inventory = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

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
            colored_cube_groups = round.split(", ")
            for group in colored_cube_groups:
                count = int(group.split(" ")[0])
                color = group.split(" ")[1]
                inventory[color] = max(inventory[color],count)

        
        game_power = 1
        for color in inventory.keys():
            game_power *= inventory[color]
        cumulative_game_power += game_power
        

print("----------------")
# 60948
print(f"Answer: {cumulative_game_power}")
            
                