from tqdm import tqdm
import copy
from skspatial.measurement import area_signed
import math

fname = "./Day18/example.txt"
fname = "./Day18/input.txt"
answer = 0


class Dig:
    def __init__(self, direction, distance, hex):
        self.direction = direction
        self.distance = distance
        self.hex = hex
        match hex[-2]:
            case "0":
                self.direction = "R"
            case "1":
                self.direction = "D"
            case "2":
                self.direction = "L"
            case "3":
                self.direction = "U"
        self.distance = int(hex[-7:-2], 16)

    def __repr__(self):
        return f"{self.direction} {self.distance} {self.hex}"


dig_plan = []
with open(fname) as f:
    for row in f.readlines():
        instruction = row.rstrip().split()
        dig = Dig(
            direction=instruction[0],
            distance=int(instruction[1]),
            hex=instruction[2]
        )
        dig_plan.append(dig)

location = [0, 0]

path = []
path.append(location)
path_length = 0
trench_count = 0
corner_count = 0

last_direction = "N"
for dig in dig_plan:
    trench_count += 1
    if dig.direction == "U":
        location = tuple([location[0]-dig.distance, location[1]])
    if dig.direction == "R":
        location = tuple([location[0], location[1]+dig.distance])
    if dig.direction == "D":
        location = tuple([location[0]+dig.distance, location[1]])
    if dig.direction == "L":
        location = tuple([location[0], location[1]-dig.distance])
    path.append(location)
    path_length += dig.distance
    if last_direction != dig.direction:
        corner_count += 1

print(abs(int(area_signed(path))), path_length, trench_count, corner_count)

print(abs(int(area_signed(path))) + int(path_length/2) +1)

print(f"Answer: {answer}")
