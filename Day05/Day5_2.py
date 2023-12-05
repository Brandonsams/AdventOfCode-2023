from tqdm import tqdm
import pandas as pd
import swifter
from pandarallel import pandarallel
pandarallel.initialize(progress_bar=True)


class almanac_section_line:
    def __init__(self, line_text):
        split_line_text = line_text.split(" ")
        self.destination_range_start = int(split_line_text[0])
        self.source_range_start = int(split_line_text[1])
        self.range_length = int(split_line_text[2])


class almanac_section:
    def __init__(self, section_text):
        lines = section_text.split("\n")
        self.title = lines[0].replace(" map:", "")
        self.source = lines[0].replace(" map:", "").split("-")[0]
        self.destination = lines[0].replace(" map:", "").split("-")[2]
        almanac_section_lines = []
        for line in lines[1:]:
            almanac_section_lines.append(almanac_section_line(line_text=line))
        self.almanac_section_lines = almanac_section_lines
        self.mapping = {}

seeds_data = []
seeds = pd.Series(dtype=float)
almanac_sections = []

fname = "./Day05/input.txt"
# fname = "./Day05/example.txt"
with open(fname) as f:
    almanac = f.read()

    almanac_sections_text = almanac.split("\n\n")

    # seeds_strings = almanac_sections_text[0].replace("seeds: ", "").split(" ")
    # for seed_range in tqdm(range(int(len(seeds_strings) / 2))):
    #     start = int(seeds_strings[2 * seed_range])
    #     length = int(seeds_strings[2 * seed_range + 1])
    #     # Fast
    #     # seeds = pd.concat([seeds, pd.Series(range(start, start + length))])
    #     # seeds = seeds.add(new_seeds)
    #     seeds_data.append(pd.Series(range(start, start + length)))
    #     print(f"Seed Count: {len(seeds_data)}")
    #     # seeds = list(set(seeds))
    #     # print(f"Seed Count: {len(seeds)}")
    #     # Slow
    #     # for i in tqdm(range(start, start + length)):
    #     #     seeds.append(int(i))

    # seeds = pd.concat(seeds_data)
    # seeds.drop_duplicates(inplace=True)

    # for seeds_string in seeds_strings:
    #     seeds.append(int(seeds_string))

    for almanac_section_text in almanac_sections_text[1:]:
        # print("-----------------")
        current_section = almanac_section(section_text=almanac_section_text)
        # print(current_section.title)

        # for line in tqdm(current_section.almanac_section_lines):
        #     for i in tqdm(range(line.range_length)):
        #         pass
        # current_section.mapping[line.source_range_start + i] = line.destination_range_start + i

        almanac_sections.append(current_section)



def get_location_by_seed(seed):
    seed_journey = [seed]
    min_location_number = 999999999999999999999
    for almanac_section in almanac_sections:
        # print(almanac_section.title)
        for almanac_section_line in almanac_section.almanac_section_lines[::-1]:

            next_journey_stage = None
            if seed_journey[-1] in range(almanac_section_line.source_range_start, almanac_section_line.source_range_start + almanac_section_line.range_length):
                next_journey_stage = (
                    seed_journey[-1] - almanac_section_line.source_range_start) + almanac_section_line.destination_range_start
                seed_journey.append(next_journey_stage)
                break
            else:
                next_journey_stage = seed_journey[-1]
                seed_journey.append(next_journey_stage)

            seed_journey.append(next_journey_stage)

        # seed_journey.append(almanac_section.mapping.get(seed_journey[-1],seed_journey[-1]))
    # print(seed_journey)
    if seed_journey[-1] < min_location_number:
        min_location_number = seed_journey[-1]
        # print(f"New minimum location: {min_location_number}")

    return min_location_number


minimums = []
with open(fname) as f:
    almanac = f.read()

    almanac_sections_text = almanac.split("\n\n")

    seeds_strings = almanac_sections_text[0].replace("seeds: ", "").split(" ")
    for seed_range in range(int(len(seeds_strings) / 2)):
        start = int(seeds_strings[2 * seed_range])
        length = int(seeds_strings[2 * seed_range + 1])
        # Fast
        # seeds = pd.concat([seeds, pd.Series(range(start, start + length))])
        # seeds = seeds.add(new_seeds)
        df = pd.Series(range(start, start + length))
        print(f"Seed Count: {df.shape[0]}")
        # seeds = list(set(seeds))
        # print(f"Seed Count: {len(seeds)}")
        # Slow
        # for i in tqdm(range(start, start + length)):
        #     seeds.append(int(i))

        # print("A")
        df = df.to_frame(name="SEEDS")
        # df = pd.DataFrame(data=seeds,columns=["SEEDS"])
        # print("B")
        # seeds = seeds.drop_duplicates()
        # df["LOCATION"] = df["SEEDS"].swifter.progress_bar(False).apply(get_location_by_seed)
        df["LOCATION"] = df["SEEDS"].parallel_apply(get_location_by_seed)
        minimum = df['LOCATION'].min()
        print(minimum)
        minimums.append(minimum)

print(f"Answer: {min(minimums)}, {minimums}")

    # seeds = pd.concat(seeds_data)
    # seeds.drop_duplicates(inplace=True)

# print("A")
# seeds = seeds.to_frame(name="SEEDS")
# # df = pd.DataFrame(data=seeds,columns=["SEEDS"])
# # print("B")
# # seeds = seeds.drop_duplicates()
# seeds["LOCATION"] = seeds.map(lambda seed: get_location_by_seed(seed=seed))
# print(seeds['LOCATION'].min())


# min_location_number = 999999999999999999999
# for seed in tqdm(seeds):
#     seed_journey = [seed]
#     for almanac_section in almanac_sections:
#         # print(almanac_section.title)
#         for almanac_section_line in almanac_section.almanac_section_lines[::-1]:

#             next_journey_stage = None
#             if seed_journey[-1] in range(almanac_section_line.source_range_start, almanac_section_line.source_range_start + almanac_section_line.range_length):
#                 next_journey_stage = (seed_journey[-1] - almanac_section_line.source_range_start) + almanac_section_line.destination_range_start
#                 seed_journey.append(next_journey_stage)
#                 break
#             else:
#                 next_journey_stage = seed_journey[-1]
#                 seed_journey.append(next_journey_stage)


#             seed_journey.append(next_journey_stage)

#         # seed_journey.append(almanac_section.mapping.get(seed_journey[-1],seed_journey[-1]))
#     # print(seed_journey)
#     if seed_journey[-1] < min_location_number:
#         min_location_number = seed_journey[-1]
#         print(f"New minimum location: {min_location_number}")

# print(f"Answer: {min_location_number}")
