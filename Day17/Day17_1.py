from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

fname = "./Day17/example.txt"
fname = "./Day17/input.txt"
answer = 0

matrix = []
with open(fname) as f:
    row_id = 0
    for row in f.readlines():
        matrix.append([])
        row = row.rstrip()
        col_id = 0
        for col in row:
            matrix[row_id].append(int(col))
            col_id += 1
        row_id += 1

grid = Grid(matrix=matrix)
start = grid.node(0, 0)
end = grid.node(row_id-1, col_id-1)

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)

print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))

# print(matrix)

print(f"Answer: {answer}")
