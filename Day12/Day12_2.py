from tqdm import tqdm
import itertools
import math

fname = "./Day12/example.txt"
# fname = "./Day12/input.txt"
answer = 0
folding_factor = 1


class SpringRow:

    def __init__(self, row):
        self.row = row

        self.split_row = row.split(" ")
        self.springs = "?".join([self.split_row[0]
                                for f in range(folding_factor)])
        self.damage_record = ",".join(
            [self.split_row[1] for f in range(folding_factor)])

        self.spring_count = len(self.springs)
        self.operational_spring_count = self.springs.count(".")
        self.damaged_spring_count = self.springs.count("#")
        self.unknown_spring_count = self.springs.count("?")

        self.unknown_spring_indices = [
            i for i, ltr in enumerate(self.springs) if ltr == "?"]

        self.recorded_damaged_spring_count = sum(
            map(int, self.damage_record.split(",")))
        self.missing_damaged_spring_count = self.recorded_damaged_spring_count - \
            self.damaged_spring_count

    def count_arrangements(self):
        pass


with open(fname) as f:
    for row in tqdm(f.readlines()):
        row_answer = 0
        row = row.rstrip()
        spring_row = SpringRow(row=row)
        x_combs = itertools.combinations(
            iterable=spring_row.unknown_spring_indices, r=spring_row.missing_damaged_spring_count)
        prev_x_comb = []
        prev_failed_replace_index = 0
        temp_springs = spring_row.springs
        for x_comb in tqdm(x_combs, total=math.comb(len(spring_row.unknown_spring_indices), spring_row.missing_damaged_spring_count)):
            if len(prev_x_comb) > 0 and list(x_comb)[:len(prev_x_comb)] == prev_x_comb:
                print(x_comb)
                continue
            temp_springs = temp_springs[:prev_failed_replace_index] + \
                "?" + temp_springs[prev_failed_replace_index + 1:]
            comb_is_good = True
            if prev_failed_replace_index == 0:
                # prev_failed_replace_index = spring_row.missing_damaged_spring_count
                pass
            for replace_index in x_comb[prev_failed_replace_index:]:
                temp_springs = temp_springs[:replace_index] + \
                    "#" + temp_springs[replace_index + 1:]
                temp_springs_slice = temp_springs[:replace_index + 1]
                temp_damage_record = ",".join(list(map(str, map(len, " ".join(
                    temp_springs_slice.replace("?", ".").split(".")).split()))))
                if not spring_row.damage_record.startswith(temp_damage_record):
                    prev_failed_replace_index = replace_index
                    prev_x_comb = list(x_comb[:replace_index])
                    comb_is_good = False
                    break
            if comb_is_good:
                # print(comb_is_good)
                temp_springs = spring_row.springs
                for replace_index in x_comb:
                    temp_springs = (
                        temp_springs[:replace_index] + "#" + temp_springs[replace_index + 1:])
                temp_springs = temp_springs.replace("?", ".")
                temp_springs_damage_record = ",".join(
                    list(map(str,
                             map(len, " ".join(temp_springs.split(".")).split()))
                         ))
                if temp_springs_damage_record == spring_row.damage_record:
                    row_answer += 1
        answer += row_answer
        print(f"{spring_row.row} --- {row_answer}")



print(f"Answer: {answer}")
