from tqdm import tqdm
import copy

fname = "./Day18/example.txt"
fname = "./Day18/input.txt"
answer = 0


class Dig:
    def __init__(self, direction, distance, hex):
        self.direction = direction
        self.distance = distance
        self.hex = hex

    def __repr__(self):
        return f"{self.direction} {self.distance} {self.hex}"


def dirt_map_to_str(dirt_map):
    rows = []
    for row in dirt_map:
        rows.append(str.join("", row))
    return str.join("\n", rows)


dig_plan = []
with open(fname) as f:
    for row in f.readlines():
        instruction = row.rstrip().split()
        dig = Dig(
            direction=instruction[0],
            distance=int(instruction[1]),
            hex=instruction[2]
        )
        dig_plan.append(dig)

size = 1001
location = (int((size+1)/2), int((size+1)/2))

dirt_map = []
for row in range(size):
    dirt_row = []
    for col in range(size):
        dirt_row.append(".")
    dirt_map.append(dirt_row)

dirt_map[location[0]][location[1]] = "#"
for dig in dig_plan:
    # print(dig)
    for d in range(dig.distance):
        if dig.direction == "U":
            location = tuple([location[0]-1, location[1]])
        if dig.direction == "R":
            location = tuple([location[0], location[1]+1])
        if dig.direction == "D":
            location = tuple([location[0]+1, location[1]])
        if dig.direction == "L":
            location = tuple([location[0], location[1]-1])
        dirt_map[location[0]][location[1]] = "#"

# row_id = 0
# for row in dirt_map:
#     col_id = 0
#     entered_loop = False
#     prev_col = "."
#     for col in row:
#         # count the number of hash to right
#         right_hashes = row[col_id:].count("#")
#         if right_hashes % 2 == 1:
#             # dirt_map[row_id][col_id] = "#"
#             pass
#         col_id += 1
#     row_id += 1


def flood_fill_dirt_map(dirt_map):
    dirt_map_rv = copy.deepcopy(dirt_map)

    start = (0, 0)

    fill_coords = set()
    fill_coords.add(start)

    filled_more = True
    while filled_more:
        filled_more = False
        new_coords = set()
        for fill_coord in tqdm(fill_coords, desc=f"fill_coords: {len(fill_coords)}"):
            # look around
            up = tuple([fill_coord[0]-1, fill_coord[1]])
            down = tuple([fill_coord[0]+1, fill_coord[1]])
            left = tuple([fill_coord[0], fill_coord[1]-1])
            right = tuple([fill_coord[0], fill_coord[1]+1])
            neighbors = [up, down, left, right]
            for neighbor in neighbors:
                if neighbor in fill_coords:
                    continue
                if neighbor[0] < 0:
                    continue
                if neighbor[1] < 0:
                    continue
                if neighbor[0] >= len(dirt_map_rv[0]):
                    continue
                if neighbor[1] >= len(dirt_map_rv):
                    continue
                if dirt_map[neighbor[0]][neighbor[1]] == ".":
                    filled_more = True
                    new_coords.add(neighbor)
        for new_coord in new_coords:
            fill_coords.add(new_coord)
    for fill_coord in fill_coords:
        dirt_map_rv[fill_coord[0]][fill_coord[1]] = " "

    return dirt_map_rv

dirt_map = flood_fill_dirt_map(dirt_map=dirt_map)

row_id = 0
for row in dirt_map:
    col_id = 0
    for col in row:
        if dirt_map[row_id][col_id] == ".":
            dirt_map[row_id][col_id] = "#"
        col_id += 1
    row_id += 1

dirts = dirt_map_to_str(dirt_map=dirt_map)

# print(dirts)
print(dirts.count("#"))


print(f"Answer: {answer}")
