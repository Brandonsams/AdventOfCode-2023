from tqdm import tqdm
import itertools

fname = "./Day14/example.txt"
fname = "./Day14/input.txt"
answer = 0


def replace_char_in_string(s, char, index):
    return s[:index] + char + s[index + 1:]

lines = []
with open(fname) as f:
    f_contents = f.read()
    for line in f_contents.split("\n"):
        lines.append(line)

line_length = len(lines[0])
something_moved = True
while something_moved:
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

w = len(lines)
for line in lines:
    print(line)
    round_rock_count = line.count("O")
    answer += round_rock_count * w
    w -= 1

print(f"Answer: {answer}")
