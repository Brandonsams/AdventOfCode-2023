from tqdm import tqdm

# fname = "./Day10/example.txt"
# fname = "./Day10/example2.txt"
# fname = "./Day10/example3.txt"
# fname = "./Day10/example4.txt"
fname = "./Day10/input.txt"
answer = 0

sketch = []
start = None
start_south = None
sketch_width = 0
pipes = {"|": "NS", "-": "EW", "L": "NE",
         "J": "NW", "7": "SW", "F": "ES", "S": "ES"}
directions = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}


class Coord:

    def __init__(self, row_index, column_index):
        self.row_index = row_index
        self.column_index = column_index

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Coord):
            return self.row_index == other.row_index and self.column_index == other.column_index
        return False
    
    def __str__(self):
        return f"({self.row_index},{self.column_index})"


class Tile:

    def __init__(self, icon, coord):
        self.icon = icon
        self.coord = coord
        self.distance_from_start = 0
        self.connecting_coords = []
        for connection_direction in pipes.get(icon, ""):
            adjustment = directions[connection_direction]
            coord_tuple = (coord.row_index, coord.column_index)
            new_tuple = tuple([sum(x) for x in zip(adjustment, coord_tuple)])
            if new_tuple[0] < 0 or new_tuple[1] < 0:
                continue
            self.connecting_coords.append(
                Coord(row_index=new_tuple[0], column_index=new_tuple[1]))


with open(fname) as f:
    row = 0
    for line in tqdm(f.readlines()):
        line = line.rstrip()
        sketch_width = len(line)
        sketch.append(line)
        if "S" in line:
            col = line.index("S")
            start = Coord(row_index=row,column_index=col)
            start_south = Coord(row_index=row + 1,column_index=col)
        row += 1


tiles = []
tiles_by_row = []
row_index = 0
for sketch_row in sketch:
    col_index = 0
    this_row_tiles = []
    for sketch_col in sketch_row:
        new_tile = Tile(icon=sketch_col, coord=Coord(
            row_index=row_index, column_index=col_index))
        tiles.append(new_tile)
        this_row_tiles.append(new_tile)
        col_index += 1
    tiles_by_row.append(this_row_tiles)
    row_index += 1


def get_next_tile(prev_tile, current_tile):
    temp_connecting_coords = current_tile.connecting_coords.copy()
    temp_connecting_coords.remove(prev_tile.coord)
    remaining_coord = temp_connecting_coords[0]

    next_tile = [tile for tile in tiles if tile.coord == remaining_coord][0]
    return next_tile

pipe_loop = []

current_tile = [tile for tile in tiles if tile.coord == start][0]
prev_tile = [tile for tile in tiles if tile.coord == start_south][0]
next_tile = get_next_tile(prev_tile=prev_tile,current_tile=current_tile)
pipe_loop.append(current_tile)

counter = 0
while not next_tile.icon == "S":
    counter += 1
    if counter % 100 == 0:
        print(counter)
    next_tile = get_next_tile(prev_tile=prev_tile,current_tile=current_tile)
    prev_tile = current_tile
    current_tile = next_tile
    pipe_loop.append(current_tile)

inside_tiles = []
for tile in tqdm(tiles):
    if tile not in pipe_loop:
        # walk right (or left?) and count the number of vertical sections in the pipe loop
        this_row = tiles_by_row[tile.coord.row_index]

        pipe_loop_intersections = 0
        pipe_intersections_dict = {}

        for row_tile in this_row:
            if row_tile == tile:
                break
            if row_tile in pipe_loop:
                if row_tile.icon in [pipe for pipe in pipes.keys() if not pipe in ["-","7","F","S"]]:
                    pipe_loop_intersections += 1
                    pipe_intersections_dict[row_tile.icon] = pipe_intersections_dict.get(row_tile.icon, 0) + 1
        if pipe_loop_intersections % 2 == 1:
            # print(tile.coord)
            inside_tiles.append(tile)

print(f"Answer: {len(inside_tiles)}")
