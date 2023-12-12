from tqdm import tqdm
import itertools

fname = "./Day11/example.txt"
fname = "./Day11/input.txt"
answer = 0

lines = []
with open(fname) as f:
    for line in tqdm(f.readlines()):
        line = line.rstrip()
        lines.append(line)
        line_chars = "".join(set(line))
        if len(line_chars) == 1 and line_chars[0] == ".":
            lines.append(line)

transposed_lines = ["".join(col) for col in zip(*lines)]
transposed_expanded_lines = []
for transposed_line in transposed_lines:
    transposed_expanded_lines.append(transposed_line)
    transposed_line_chars = "".join(set(transposed_line))
    if len(transposed_line_chars) == 1 and transposed_line_chars[0] == ".":
        transposed_expanded_lines.append(transposed_line)

transposed_transposed_lines = ["".join(col)
                               for col in zip(*transposed_expanded_lines)]

expanded_lines = transposed_expanded_lines

galaxy_coords = []
row = 0
for expanded_line in expanded_lines:
    col = 0
    for char in expanded_line:
        if char == "#":
            galaxy_coords.append((row, col))
        col += 1
    row += 1

galaxy_coords_pairs = set(itertools.combinations(galaxy_coords, r=2))
for galaxy_coords_pair in galaxy_coords_pairs:
    a = galaxy_coords_pair[0]
    b = galaxy_coords_pair[1]
    answer += abs(a[0]-b[0]) + abs(a[1]-b[1])

print(f"Answer: {answer}")
