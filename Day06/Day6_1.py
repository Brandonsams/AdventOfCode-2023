from math import sqrt, ceil, floor

times = []
distances = []
race_margins = []

fname = "./Day06/input.txt"
# fname = "./Day06/example.txt"
with open(fname) as f:
    for line in f.readlines():
        line = line.rstrip()
        line_data = line.split()
        if line_data[0] == "Time:":
            for data in line_data[1:]:
                times.append(float(data))
        else:
            for data in line_data[1:]:
                distances.append(float(data))

for time, distance in zip(times, distances):
    lower_margin = ((time - sqrt((time * time) - (4 * distance))) / 2.0) + 0.00001
    upper_margin = ((time + sqrt((time * time) - (4 * distance))) / 2.0) - 0.00001
    race_margin = floor(upper_margin) - ceil(lower_margin) + 1
    race_margins.append(race_margin)

race_margin_product = 1
for race_margin in race_margins:
    race_margin_product *= race_margin

print(f"Answer: {race_margin_product}")