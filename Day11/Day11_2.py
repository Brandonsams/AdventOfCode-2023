from tqdm import tqdm
import itertools

fname = "./Day11/example.txt"
fname = "./Day11/input.txt"
answer = 0
expansion_factor = 1000000 - 1

expanded_row_indices = []
expanded_col_indices = []

lines = []
with open(fname) as f:
    row = 0
    for line in tqdm(f.readlines()):
        line = line.rstrip()
        lines.append(line)
        line_chars = "".join(set(line))
        if len(line_chars) == 1 and line_chars[0] == ".":
            expanded_row_indices.append(row)
        row += 1

transposed_lines = ["".join(col) for col in zip(*lines)]
transposed_expanded_lines = []
col = 0
for transposed_line in tqdm(transposed_lines):
    transposed_expanded_lines.append(transposed_line)
    transposed_line_chars = "".join(set(transposed_line))
    if len(transposed_line_chars) == 1 and transposed_line_chars[0] == ".":
        expanded_col_indices.append(col)
    col += 1

transposed_transposed_lines = ["".join(col)
                               for col in zip(*transposed_expanded_lines)]

expanded_lines = transposed_transposed_lines

galaxy_coords = []
row = 0
for expanded_line in tqdm(expanded_lines):
    col = 0
    for char in expanded_line:
        if char == "#":
            galaxy_coords.append((row, col))
        col += 1
    row += 1

galaxy_coords_pairs = set(itertools.combinations(galaxy_coords, r=2))
for galaxy_coords_pair in tqdm(galaxy_coords_pairs):
    a = galaxy_coords_pair[0]
    b = galaxy_coords_pair[1]

    expanded_row_count_between_coords = 0
    for expanded_row_index in expanded_row_indices:
        if expanded_row_index in range(a[0], b[0]) or expanded_row_index in range(b[0], a[0]):
            expanded_row_count_between_coords += 1

    expanded_col_count_between_coords = 0
    for expanded_col_index in expanded_col_indices:
        if expanded_col_index in range(a[1], b[1]) or expanded_col_index in range(b[1], a[1]):
            expanded_col_count_between_coords += 1

    galaxy_distance = abs(a[0]-b[0]) + expanded_row_count_between_coords * expansion_factor + \
        abs(a[1]-b[1]) + expanded_col_count_between_coords * expansion_factor

    answer += galaxy_distance

print(f"Answer: {answer}")
