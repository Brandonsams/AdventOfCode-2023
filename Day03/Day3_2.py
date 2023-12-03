part_number_data_example = [
    {
        "part_number": 467,
        "coords": [
            [2, 4],
            [2, 5],
            [2, 6]
        ]
    }
]

gear_data_example = [
    [2, 5],
    [13, 0]
]

part_number_data = [

]

gear_data = [

]


digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
allowed_neighbor_values = digits + ['.']


def get_coords_in_neighborhood(row_index, column_index):
    rv = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            rv.append([row_index + i, column_index + j])
    return rv


def add_part_number_data(part_number, row_index, column_index):
    rv = {
        "part_number": part_number,
        "coords": [
        ]
    }

    for digit_index in range(len(part_number)):
        rv["coords"].append([row_index, column_index + digit_index])

    part_number_data.append(rv)


def has_disallowed_symbols_in_neighborhood(rows, row_index, column_index, allowed_neighbor_values):

    min_row_index = 0
    max_row_index = len(rows) - 1
    min_column_index = 0
    max_column_index = len(rows[row_index]) - 1

    # Prev Row
    if row_index != min_row_index:
        if rows[row_index - 1][column_index] not in allowed_neighbor_values:
            return True
        if column_index != min_column_index and rows[row_index - 1][column_index - 1] not in allowed_neighbor_values:
            return True
        if column_index != max_column_index and rows[row_index - 1][column_index + 1] not in allowed_neighbor_values:
            return True

    # Current row
    if column_index > min_column_index and rows[row_index][column_index - 1] not in allowed_neighbor_values:
        return True
    if column_index != max_column_index and rows[row_index][column_index + 1] not in allowed_neighbor_values:
        return True

    # Next Row
    if row_index != max_row_index:
        if rows[row_index + 1][column_index] not in allowed_neighbor_values:
            return True
        if column_index != min_column_index and rows[row_index + 1][column_index - 1] not in allowed_neighbor_values:
            return True
        if column_index != max_column_index and rows[row_index + 1][column_index + 1] not in allowed_neighbor_values:
            return True

    # We good
    return False


rows = []
fname = "./Day03/input.txt"
# fname = "./Day03/example.txt"
# fname = "./Day03/example2.txt"
with open(fname) as f:
    row_index = 0
    for row in f.readlines():
        row = row.rstrip()
        rows.append(row)

cumulative_part_numbers = 0
cumulative_all_numbers = 0
row_index = 0
for row in rows:
    print(row)

    # found_num_start = False
    # found_num_end = False
    is_in_number = False

    row_part_numbers = []
    possible_part_number = ''
    is_part_number = False

    for column_index in range(len(row)):
        if row[column_index] == "*":
            gear_data.append([row_index, column_index])

        if row[column_index] in digits:
            is_in_number = True
            possible_part_number += row[column_index]
            if has_disallowed_symbols_in_neighborhood(
                rows=rows,
                row_index=row_index,
                column_index=column_index,
                allowed_neighbor_values=allowed_neighbor_values
            ):
                is_part_number = True
            if is_part_number and column_index == (len(row) - 1):
                add_part_number_data(part_number=possible_part_number, row_index=row_index, column_index=(
                    column_index - len(possible_part_number) + 1))

                row_part_numbers.append(possible_part_number)
                cumulative_all_numbers += int(possible_part_number)

        else:
            if is_in_number:
                # we found the end of a number, add it to the list if it is a part number
                if is_part_number:
                    add_part_number_data(part_number=possible_part_number, row_index=row_index, column_index=(
                        column_index - len(possible_part_number)))

                    row_part_numbers.append(possible_part_number)
                else:
                    print(possible_part_number)
                cumulative_all_numbers += int(possible_part_number)
                possible_part_number = ''
                is_part_number = False
            is_in_number = False

    # print(row_part_numbers)
    for row_part_number in row_part_numbers:
        cumulative_part_numbers += int(row_part_number)

    row_index += 1


# --------------------------

cumulative_gear_ratio = 0
for gear in gear_data:
    gear_neighborhood = get_coords_in_neighborhood(
        row_index=gear[0], column_index=gear[1])

    nearby_parts = []
    for part in part_number_data:
        for part_coord in part["coords"]:
            if part_coord in gear_neighborhood:
                nearby_parts.append(part)
                break
    if len(nearby_parts) == 2:
        gear_ratio = int(nearby_parts[0]["part_number"]) * \
            int(nearby_parts[1]["part_number"])
        cumulative_gear_ratio += gear_ratio

# print(f"all: {cumulative_all_numbers}")
print(f"answer: {cumulative_gear_ratio}")
