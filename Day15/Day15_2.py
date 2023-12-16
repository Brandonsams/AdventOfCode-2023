from tqdm import tqdm

fname = "./Day15/example.txt"
fname = "./Day15/input.txt"
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

boxes = {}
for b in range(256):
    boxes[b] = []

for step in steps:
    label = None
    box = None
    operation_character = None
    focal_length = None

    if "-" in step:
        operation_character = "-"
        label = step.split("-")[0]
        box = hash(label)
        for lens in boxes[box]:
            if lens[0] == label:
                boxes[box].remove(lens)

    else:
        operation_character = "="
        label = step.split("=")[0]
        focal_length = int(step.split("=")[1])
        box = hash(label)
        i = 0
        for lens in boxes[box]:
            if lens[0] == label:
                boxes[box][i] = (label, focal_length)
                break
            i += 1
        else:
            boxes[box].append((label, focal_length))

for b in range(256):
    for l, lens in zip(range(len(boxes[b])), boxes[b]):
        answer += (b+1)*(l+1)*(lens[1])


print(f"Answer: {answer}")
