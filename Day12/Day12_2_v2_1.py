from tqdm import tqdm
import itertools
import math

fname = "./Day12/example.txt"
fname = "./Day12/input.txt"
answer = 0
folding_factor = 5


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


def check_damage_record(springs_sub, damage_record):
    damage_record_sub = ",".join(
        list(
            map(
                str, map(
                    len, " ".join(
                        springs_sub.split(".")
                    ).split()
                )
            )
        )
    )

    last_num_good = True
    try:
        comma_count = damage_record_sub.count(",")
        last_num_sub = int(damage_record_sub.split(",")[comma_count])
        last_num_record = int(damage_record.split(",")[comma_count])
        last_num_good = last_num_sub <= last_num_record
    except:
        pass

    damage_record_sub_no_last_num = damage_record_sub[:damage_record_sub.rfind(
        ",")]

    rv = damage_record.startswith(
        damage_record_sub_no_last_num) and last_num_good
    return rv


spring_rows = []
with open(fname) as f:
    for row in f.readlines():
        row = row.rstrip()
        spring_rows.append(SpringRow(row=row))

count = 0
for spring_row in tqdm(spring_rows):
    count+=1
    # print(spring_row.springs)
    # print(spring_row.damage_record)
    spring_pointer = 0
    springs_sub = ""
    spring_subs = ['']
    while spring_pointer < len(spring_row.springs):

        if spring_row.springs[spring_pointer:].count("?") == 0:
            pass

        # springs_sub = spring_row.springs[:spring_pointer]
        desc = f"| {count} of {len(spring_rows)} | {spring_pointer + 1} of {len(spring_row.springs)} |"

        s = []
        temp = [spring_sub for spring_sub in spring_subs if len(spring_sub) == spring_pointer]
        for i in tqdm(range(len(temp))):
        # for spring_sub in [spring_sub for spring_sub in spring_subs if len(spring_sub) == spring_pointer]:
            spring_sub = temp.pop()

            damaged_springs_count = spring_sub.count("#")
            remaining_damaged_springs_count = spring_row.springs[spring_pointer:].count("#")
            remaining_mystery_count = spring_row.springs[spring_pointer:].count("?")

            if spring_row.recorded_damaged_spring_count > damaged_springs_count + remaining_damaged_springs_count + remaining_mystery_count:
                continue

            # if spring_row.recorded_damaged_spring_count > len(spring_row.springs) - spring_sub.count("#"):
            #     continue

            if spring_row.springs[spring_pointer] == "?":
                t = spring_sub + "."
                if t.count("#") <= spring_row.recorded_damaged_spring_count:
                    if check_damage_record(springs_sub=t, damage_record=spring_row.damage_record):
                        spring_subs.append(t)

                t  = spring_sub + "#"
                if t.count("#") <= spring_row.recorded_damaged_spring_count:
                    if check_damage_record(springs_sub=t, damage_record=spring_row.damage_record):
                        spring_subs.append(t)
            else:
                t = spring_sub + spring_row.springs[spring_pointer]
                if t.count("#") <= spring_row.recorded_damaged_spring_count:
                    if check_damage_record(springs_sub=t, damage_record=spring_row.damage_record):
                        spring_subs.append(t)

        # for t in tqdm(s, desc=desc):
        #     if t.count("#") <= spring_row.recorded_damaged_spring_count:
        #         if check_damage_record(springs_sub=t, damage_record=spring_row.damage_record):
        #             spring_subs.append(t)
        spring_pointer += 1

    for x in [spring_sub for spring_sub in spring_subs if len(spring_sub) == spring_pointer]:
        # print(x)
        damage_record_sub = ",".join(
            list(
                map(
                    str, map(
                        len, " ".join(
                            x.split(".")
                        ).split()
                    )
                )
            )
        )
        if damage_record_sub == spring_row.damage_record:
            answer += 1
        else:
            pass


print(f"Answer: {answer}")
