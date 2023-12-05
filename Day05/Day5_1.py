from tqdm import tqdm

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

seeds = []
almanac_sections = []

fname = "./Day05/input.txt"
# fname = "./Day05/example.txt"
with open(fname) as f:
    almanac = f.read()

    almanac_sections_text = almanac.split("\n\n")

    seeds_strings = almanac_sections_text[0].replace("seeds: ","").split(" ")
    for seeds_string in seeds_strings:
        seeds.append(int(seeds_string))

    for almanac_section_text in almanac_sections_text[1:]:
        print("-----------------")
        current_section = almanac_section(section_text=almanac_section_text)
        print(current_section.title)

        for line in current_section.almanac_section_lines:
            for i in tqdm(range(line.range_length)):
                current_section.mapping[line.source_range_start + i] = line.destination_range_start + i
        
        almanac_sections.append(current_section)

min_location_number = 999999999999999999999
for seed in seeds:
    seed_journey = [seed]
    for almanac_section in almanac_sections:
        seed_journey.append(almanac_section.mapping.get(seed_journey[-1],seed_journey[-1]))
    print(seed_journey)
    min_location_number = min(min_location_number,seed_journey[-1])

print(f"Answer: {min_location_number}")