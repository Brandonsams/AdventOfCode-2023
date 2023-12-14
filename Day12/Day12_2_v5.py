from tqdm import tqdm
import itertools
import math
import numpy as np


fname = "./Day12/example.txt"
# fname = "./Day12/input.txt"
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

        self.damage_record_list = [int(d)
                                   for d in self.damage_record.split(",")]

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


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def fast_comb(n, k):
    a = np.ones((k, n-k+1), dtype=int)
    a[0] = np.arange(n-k+1)
    for j in range(1, k):
        reps = (n-k+j) - a[j-1]
        a = np.repeat(a, reps, axis=1)
        ind = np.add.accumulate(reps)
        a[j, ind[:-1]] = 1-reps[1:]
        a[j, 0] = j
        a[j] = np.add.accumulate(a[j])
    return a


def stars_and_bars(num_stars, num_bars):
    stars = "." * num_stars
    fb = fast_comb(n=num_bars, k=num_stars+1)


def count_partitions(n, k):
    # n+k-1 choose k-1
    return math.comb(n+k-1, k-1)


def partitions(n, k):
    for c in itertools.combinations(range(n+k-1), k-1):
        yield [b-a-1 for a, b in zip((-1,)+c, c+(n+k-1,))]


def string_insert(source_str, insert_str, pos):
    return source_str[:pos] + insert_str + source_str[pos:]


answer = 0
with open(fname) as f:
    row_id = 0
    for row in f.readlines():
        row_answer = 0
        row = row.rstrip()
        spring_row = SpringRow(row=row)

        m = ".".join([d*"#" for d in spring_row.damage_record_list])
        insertions = [0] + find(s=m, ch=".") + [len(spring_row.springs)-1]
        spring_opts = []

        # print(f"{(len(spring_row.springs) - len(m))} * {(len(insertions))} = {(len(spring_row.springs) - len(m)) * (len(insertions))}")

        partitions_count = count_partitions(
            (len(spring_row.springs) - len(m)), len(insertions))
        # for partition in tqdm(partitions((len(spring_row.springs) - len(m)), len(insertions)), total=partitions_count):
        temp_m = m
        # print(partition)

        p = 0
        while len(temp_m) < len(spring_row.springs):
            s = spring_row.springs[p]
            t = temp_m[p]
                # if i < p:
                #     continue
            if s == "?" or s == t:
                p += 1
            else:
                # old_temp_m = temp_m
                temp_m = string_insert(temp_m,".",p)
            # else:
            #     row_answer += 1
            #     answer += 1

        # now check temp_m against spring_row.springs
        good_string = True
        for a, b in zip(spring_row.springs, temp_m):
            if a == "?":
                continue
            if not a == b:
                good_string = False
                break
        if good_string:
            row_answer += 1
            answer += 1

        #     good_so_far = True
        #     for part_id, insert_id in zip(partition[::-1], insertions[::-1]):
        #         if part_id == 0:
        #             continue
        #         temp_m = string_insert(
        #             source_str=temp_m, insert_str="."*part_id, pos=insert_id)
        #         p = len(temp_m)-1
        #         for a, b in zip(spring_row.springs[::-1], temp_m[::-1]):
        #             if a == "?":
        #                 continue
        #             if not a == b:
        #                 good_so_far = False
        #                 break
        #             p -= 1
        #         if not good_so_far:
        #             break
        #     if not good_so_far:
        #         continue
        #         # print(temp_m)

        #     # now check temp_m against spring_row.springs
        #     good_string = True
        #     for a, b in zip(spring_row.springs, temp_m):
        #         if a == "?":
        #             continue
        #         if not a == b:
        #             good_string = False
        #             break
        #     if good_string:
        #         row_answer += 1
        #         answer += 1
        # print(f"row {row_id}: {row_answer}")
        # break
        # print(m)
        # answer += (len(spring_row.springs) - len(m)) * (len(insertions))
        # for i in range(len(spring_row.springs) - len(m)):
        #     # we have i dots to insert, and they can be inserted at any of insertions
        #     pass

        # x_combs = itertools.combinations(
        #     iterable=spring_row.unknown_spring_indices, r=spring_row.missing_damaged_spring_count)
        # for x_comb in x_combs:
        #     temp_springs = spring_row.springs
        #     for replace_index in x_comb:
        #         temp_springs = temp_springs[:replace_index] + \
        #             "#" + temp_springs[replace_index + 1:]
        #     temp_springs = temp_springs.replace("?", ".")
        #     temp_springs_damage_record = ",".join(
        #         list(map(str,
        #                  map(len, " ".join(temp_springs.split(".")).split()))
        #              ))
        #     if temp_springs_damage_record == spring_row.damage_record:
        #         row_answer += 1
        # answer += row_answer
        # print(f"{spring_row.row} --- {row_answer}")


print(f"Answer: {answer}")
