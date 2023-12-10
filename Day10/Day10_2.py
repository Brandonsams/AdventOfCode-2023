from tqdm import tqdm

fname = "./Day09/example.txt"
# fname = "./Day09/input.txt"
answer = 0

with open(fname) as f:
    f_index = 0
    for line in tqdm(f.readlines()):
        line = line.rstrip()


print(f"Answer: {answer}")