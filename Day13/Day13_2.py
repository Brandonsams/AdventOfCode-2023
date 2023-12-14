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


def get_lines_above_h_symm(input_str):
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


def get_lines_above_h_symm_with_smudge(input_str):
    lines = input_str.split("\n")
    p = 0
    s = -1
    found_smudge = False
    while p < len(lines) - 1:
        smudge_found = False
        if lines[p] == lines[p+1] or is_one_string_smudged(lines[p], lines[p+1]):
            smudge_found = is_one_string_smudged(lines[p], lines[p+1])
            # started symmetry
            s = 1
            while p-s >= 0 and p+1+s < len(lines):
                if lines[p-s] == lines[p+1+s]:
                    s += 1
                elif not smudge_found and is_one_string_smudged(lines[p-s], lines[p+1+s]):
                    smudge_found = True
                    s += 1
                else:
                    break
            else:
                if smudge_found:
                    return p + 1
        p += 1
    return 0


def is_one_string_smudged(str_a, str_b):
    found_smudge = False
    for char_a, char_b in zip(str_a, str_b):
        if char_a != char_b:
            if found_smudge:
                return False
            found_smudge = True
    else:
        return found_smudge


patterns = []
with open(fname) as f:
    f_contents = f.read()
    for pattern in f_contents.split("\n\n"):
        patterns.append(pattern)

for pattern in patterns:
    print()
    print(pattern)

    h_symm = get_lines_above_h_symm(pattern)
    v_symm = get_lines_above_h_symm(transpose(pattern))

    h_symm_smudge = get_lines_above_h_symm_with_smudge(pattern)
    v_symm_smudge = get_lines_above_h_symm_with_smudge(
        transpose(pattern))

    answer += 100 * h_symm_smudge + v_symm_smudge


print(f"Answer: {answer}")
