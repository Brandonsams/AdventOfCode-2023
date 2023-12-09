from tqdm import tqdm

# fname = "./Day09/example.txt"
fname = "./Day09/input.txt"

prev_history_items = []

def is_all_zeros(candidate_list: [int]) -> bool:
    return len(set(candidate_list)) == 1 and list(set(candidate_list))[0] == 0

with open(fname) as f:
    f_index = 0
    for line in f.readlines():
        line = line.rstrip()
        diffs_start_collection = []
        diffs = [int(n) for n in line.split()]
        diffs_all_zero = is_all_zeros(candidate_list=diffs)
        while not diffs_all_zero:
            diffs_start_collection.append(diffs[0])
            lefts = diffs[:-1]
            rights = diffs[1:]
            diffs = [right - left for (left, right) in zip(lefts, rights)]
            diffs_all_zero = is_all_zeros(candidate_list=diffs)
        prev_history_item = 0
        for diffs_start in diffs_start_collection[::-1]:
            prev_history_item = diffs_start - prev_history_item
        prev_history_items.append(prev_history_item)
print(f"Answer: {sum(prev_history_items)}")