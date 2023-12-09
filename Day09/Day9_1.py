from tqdm import tqdm

fname = "./Day09/example.txt"
fname = "./Day09/input.txt"
diffs_last_item_total = 0


def is_all_zeros(candidate_list: [int]) -> bool:
    return len(set(candidate_list)) == 1 and list(set(candidate_list))[0] == 0


with open(fname) as f:
    f_index = 0

    for line in tqdm(f.readlines()):
        line = line.rstrip()
        diffs = [int(n) for n in line.split()]

        diffs_all_zero = False
        while not diffs_all_zero:
            diffs_last_item_total += diffs[-1]
            lefts = diffs[:-1]
            rights = diffs[1:]
            diffs = [right - left for (left, right) in zip(lefts, rights)]

            diffs_all_zero = is_all_zeros(candidate_list=diffs)

print(diffs_last_item_total)
