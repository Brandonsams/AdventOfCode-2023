from tqdm import tqdm

fname = "./Day10/example.txt"
# fname = "./Day10/input.txt"
answer = 0

sketch = []
start = None
pipes = {"|": "NS", "-": "EW", "L": "NE",
         "J": "NW", "7": "SW", "F": "ES", "S": ""}
directions = ["N", "E", "S", "W"]


def get_outbound_direction(inbound_direction, row_index, column_index):
    pipe = get_pipe(row_index=row_index, column_index=column_index)
    outbound_direction = pipes[pipe].replace(inbound_direction,"")
    return outbound_direction


def get_pipe(row_index, column_index):
    pipe = sketch[row_index][column_index]
    return pipe


def get_length_loop(inbound_direction, row_index, column_index):
    
    found_start = False

    while not found_start:
        outbound_direction = get_outbound_direction(
        inbound_direction=inbound_direction, row_index=row_index, column_index=column_index)
        pipe = get_pipe(row_index=row_index, column_index=column_index)
        found_start = pipe == "S"


with open(fname) as f:
    row = 0
    for line in tqdm(f.readlines()):
        line = line.rstrip()
        sketch.append(line)
        if "S" in line:
            start = (row, line.index("S"))
        row += 1

start_pipe_N = (
    pipes.get(get_pipe(start[0] - 1, start[1] + 0), "").replace("N", ""), start[0] - 1, start[1] + 0)
start_pipe_E = (
    pipes.get(get_pipe(start[0] + 0, start[1] + 1), "").replace("E", ""), start[0] + 0, start[1] + 1)
start_pipe_S = (
    pipes.get(get_pipe(start[0] + 1, start[1] + 0), "").replace("S", ""), start[0] + 1, start[1] + 0)
start_pipe_W = (
    pipes.get(get_pipe(start[0] + 0, start[1] - 1), "").replace("W", ""), start[0] + 0, start[1] - 1)

near_start_pipes = [start_pipe_N, start_pipe_E, start_pipe_S, start_pipe_W]
for near_start_pipe in near_start_pipes:
    if not len(near_start_pipe[0]) == 1:
        continue

    x = get_length_loop(
        inbound_direction=near_start_pipe[0], row_index=near_start_pipe[1], column_index=near_start_pipe[1])


# print(f"N: {sketch[start[0] - 1][start[1]]}")
# print(f"E: {sketch[start[0] + 0][start[1] - 1]}")
# print(f"S: {sketch[start[0] + 1][start[1]]}")
# print(f"W: {sketch[start[0] + 0][start[1] + 1]}")

# print(sketch[start[0]][start[1]])

print(f"Answer: {start}")
