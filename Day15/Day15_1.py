from tqdm import tqdm

fname = "./Day15/example.txt"
# fname = "./Day15/input.txt"
answer = 0

def hash(input_str):
    rv = 0    
    for char in input_str:
        a = ord(char)
        rv += a
        rv *= 17
        rv %= 256
    return rv

steps = []
with open(fname) as f:
    f_contents = f.read()
    for step in f_contents.split(","):
        steps.append(step)

for step in steps:
    rv = 0
    rv += hash(step)
    print(f"{step} -> {rv}")
    answer += rv





print(f"Answer: {answer}")
