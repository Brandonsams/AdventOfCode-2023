# example
example_data = [
    {
        "number": 467,
        "row_index": 0,
        "number_start": 0,
        "number_length": 3
    }
]

data = [

]
digits = ['0','1','2','3','4','5','6','7','8','9']

# fname = "./Day03/input.txt"
fname = "./Day03/example.txt"
with open(fname) as f:
    row_index = 0
    for line in f.readlines():
        line = line.rstrip()
        print(line)

        found_num_start = False
        found_num_end = False

        line_index = 0
        line_nums = ['']
        while line_index < len(line):
            if line[line_index] in digits:
                line_nums[-1] += line[line_index]
            else:
                line_nums.append('')
            line_index += 1
        print(line_nums)
