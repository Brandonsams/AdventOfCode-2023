from tqdm import tqdm
import itertools

fname = "./Day13/example.txt"
# fname = "./Day13/example2.txt"
fname = "./Day13/input.txt"
answer = 0


def transpose(input_str):
    lines = input_str.split("\n")
    transposed_lines = ["".join(col) for col in zip(*lines)]
    output_str = "\n".join(transposed_lines)
    return output_str


def get_lines_above_horizontal_symmetry(input_str):
    lines = input_str.split("\n")
    p = 0
    s = -1
    while p < len(lines) - 1:
        if lines[p] == lines[p+1]:
            # started symmetry
            s = 1
            while p-s >= 0 and p+1+s < len(lines):
                if lines[p-s] != lines[p+1+s]:
                    break
                s += 1
            else:
                return p + 1
        p += 1
    return 0


patterns = []
with open(fname) as f:
    f_contents = f.read()
    for pattern in f_contents.split("\n\n"):
        patterns.append(pattern)

for pattern in patterns:
    print()
    print(pattern)

    h_symm = get_lines_above_horizontal_symmetry(pattern)
    v_symm = get_lines_above_horizontal_symmetry(transpose(pattern))

    answer += 100 * h_symm + v_symm


print(f"Answer: {answer}")
