from tqdm import tqdm
from enum import Enum
import sys

fname = "./Day16/example.txt"
fname = "./Day16/input.txt"
answer = 0

Direction = Enum("Direction", ["UP", "RIGHT", "DOWN", "LEFT"])


def get_opposite_direction(direction: Direction):
    rv = Direction(((direction.value - 1 + 2) % 4) + 1)
    return rv


def get_split_directions(direction: Direction):
    a = Direction((direction.value - 1 - 1) % 4 + 1)
    b = get_opposite_direction(a)
    return [a, b]


class Tile:
    def __init__(self, icon, row, col):
        self.icon = icon
        self.row = row
        self.col = col
        self.is_energized = False
    
    def __str__(self):
        return self.icon
    
    def __repr__(self):
        return f"({self.icon},{self.row},{self.col})"

def get_downstream_tiles(inbound_direction: Direction, tile: Tile):
    rv = []
    current_tile = (inbound_direction, tile.icon)
    match current_tile:
        case (Direction.UP, "."):
            t = next((t for t in tiles if t.row == tile.row - 1 and t.col == tile.col), None)
            rv.append((Direction.UP, t))
        case (Direction.UP, "/"):
            t = next((t for t in tiles if t.row == tile.row and t.col == tile.col + 1), None)
            rv.append((Direction.RIGHT, t))
        case (Direction.UP, "\\"):
            t = next((t for t in tiles if t.row == tile.row and t.col == tile.col - 1), None)
            rv.append((Direction.LEFT, t))
        case (Direction.UP, "-"):
            t = next((t for t in tiles if t.row == tile.row and t.col == tile.col - 1), None)
            rv.append((Direction.LEFT, t))
            t = next((t for t in tiles if t.row == tile.row and t.col == tile.col + 1), None)
            rv.append((Direction.RIGHT, t))
        case (Direction.UP, "|"):
            t = next((t for t in tiles if t.row == tile.row - 1 and t.col == tile.col), None)
            rv.append((Direction.UP, t))
        case (Direction.RIGHT, "."):
            t = next((t for t in tiles if t.row == tile.row and t.col == tile.col + 1), None)
            rv.append((Direction.RIGHT, t))
        case (Direction.RIGHT, "/"):
            t = next((t for t in tiles if t.row == tile.row - 1 and t.col == tile.col), None)
            rv.append((Direction.UP, t))
        case (Direction.RIGHT, "\\"):
            t = next((t for t in tiles if t.row == tile.row + 1 and t.col == tile.col), None)
            rv.append((Direction.DOWN, t))
        case (Direction.RIGHT, "-"):
            t = next((t for t in tiles if t.row == tile.row and t.col == tile.col + 1), None)
            rv.append((Direction.RIGHT, t))
        case (Direction.RIGHT, "|"):
            t = next((t for t in tiles if t.row == tile.row - 1 and t.col == tile.col), None)
            rv.append((Direction.UP, t))
            t = next((t for t in tiles if t.row == tile.row + 1 and t.col == tile.col), None)
            rv.append((Direction.DOWN, t))
        case (Direction.DOWN, "."):
            t = next((t for t in tiles if t.row == tile.row + 1 and t.col == tile.col), None)
            rv.append((inbound_direction, t))
        case (Direction.DOWN, "/"):
            t = next((t for t in tiles if t.row == tile.row and t.col == tile.col - 1), None)
            rv.append((Direction.LEFT, t))
        case (Direction.DOWN, "\\"):
            t = next((t for t in tiles if t.row == tile.row and t.col == tile.col + 1), None)
            rv.append((Direction.RIGHT, t))
        case (Direction.DOWN, "-"):
            t = next((t for t in tiles if t.row == tile.row and t.col == tile.col - 1), None)
            rv.append((Direction.LEFT, t))
            t = next((t for t in tiles if t.row == tile.row and t.col == tile.col + 1), None)
            rv.append((Direction.RIGHT, t))
        case (Direction.DOWN, "|"):
            t = next((t for t in tiles if t.row == tile.row + 1 and t.col == tile.col), None)
            rv.append((Direction.DOWN, t))
        case (Direction.LEFT, "."):
            t = next((t for t in tiles if t.row == tile.row and t.col == tile.col - 1), None)
            rv.append((Direction.LEFT, t))
        case (Direction.LEFT, "/"):
            t = next((t for t in tiles if t.row == tile.row + 1 and t.col == tile.col), None)
            rv.append((Direction.DOWN, t))
        case (Direction.LEFT, "\\"):
            t = next((t for t in tiles if t.row == tile.row - 1 and t.col == tile.col), None)
            rv.append((Direction.UP, t))
        case (Direction.LEFT, "-"):
            t = next((t for t in tiles if t.row == tile.row and t.col == tile.col - 1), None)
            rv.append((Direction.LEFT, t))
        case (Direction.LEFT, "|"):
            t = next((t for t in tiles if t.row == tile.row - 1 and t.col == tile.col), None)
            rv.append((Direction.UP, t))
            t = next((t for t in tiles if t.row == tile.row + 1 and t.col == tile.col), None)
            rv.append((Direction.DOWN, t))
    rv2 = [x for x in rv if x[1] is not None]
    return rv2


def visit_downstream_tiles(downstream_tiles: list[tuple[Direction, Tile]]):
    for downstream_tile in downstream_tiles:
        if not downstream_tile in visited_downstream_tiles:
            visited_downstream_tiles.append(downstream_tile)
            downstream_tile[1].is_energized = True
            # preview_tiles()
            dst = get_downstream_tiles(downstream_tile[0],downstream_tile[1])
            visit_downstream_tiles(dst)
        else:
            pass

def preview_tiles():
    sorted_tiles = sorted(tiles, key=lambda t: (t.row, t.col))
    pv = "\n"
    for t in sorted_tiles:
        if t.col == 0:
            pv += "\n"
        if t.is_energized:
            pv += "#"
        else:
            pv += "."
    # print(pv, end="\r\n")
    print(pv)


tiles = []
with open(fname) as f:
    row_id = 0
    for row in f.readlines():
        row = row.rstrip()
        col_id = 0
        for col in row:
            new_tile = Tile(icon=col, row=row_id, col=col_id)
            tiles.append(new_tile)
            col_id += 1
        row_id += 1

sys.setrecursionlimit(col_id * row_id)

start_tile = next((t for t in tiles if t.row == 0 and t.col == 0), None)
start_tile.is_energized == True
start_direction = Direction.RIGHT
start = [(start_direction, start_tile)]

visited_downstream_tiles = []
visit_downstream_tiles(start)

preview_tiles()

for tile in tiles:
    if tile.is_energized:
        answer += 1

print(f"Answer: {answer}")
