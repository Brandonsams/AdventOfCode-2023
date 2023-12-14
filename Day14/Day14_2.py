from tqdm import tqdm
import itertools

fname = "./Day14/example.txt"
fname = "./Day14/input.txt"
answer = 0


def replace_char_in_string(s, char, index):
    return s[:index] + char + s[index + 1:]

def rotate_clockwise(board):
    return ["".join(col[::-1]) for col in zip(*board)]

def tilt_up(board):
    lines = board
    line_length = len(lines[0])
    something_moved = True
    while something_moved:

        # print("\n".join(lines), end='\r')

        something_moved = False
        # loop over input
        for i in range(len(lines) - 1):
            # loop over pairs of lines
            for j, a, b in zip(range(line_length), lines[i], lines[i+1]):
                # # loop over length of line
                # for c in range(line_length):
                # do compare
                if a == "." and b == "O":
                    something_moved = True
                    
                    temp = lines[i]
                    lines[i] = replace_char_in_string(lines[i],"O",j)

                    # lines[i+1][c] = "."
                    lines[i+1] = replace_char_in_string(lines[i+1],".",j)
    return lines

def spin_cycle(board):
    temp_board = board
    for spin in range(4):
        temp_board = rotate_clockwise(tilt_up(board=temp_board))
        # print("\n".join(temp_board))
    return temp_board

def calculate_load(board):
    rv = 0
    w = len(board)
    for line in board:
        print(line)
        round_rock_count = line.count("O")
        rv += round_rock_count * w
        w -= 1
    return rv
    


board = []
with open(fname) as f:
    f_contents = f.read()
    for line in f_contents.split("\n"):
        board.append(line)

cycle_history = {}
max_cycle_count = 1000000000
for cycle in range(max_cycle_count):
    board = spin_cycle(board=board)
    board_str = "\n".join(board)
    print("-" *120)
    print(board_str, end='\r')

    if board_str in cycle_history:
        prev_count = cycle_history[board_str]
        period = cycle - prev_count
        remainder = (max_cycle_count-prev_count) % period
        for r in range(remainder-1):
            board = spin_cycle(board=board)
        break
    else:
        cycle_history[board_str] = cycle

answer = calculate_load(board=board)

print(f"Answer: {answer}")
