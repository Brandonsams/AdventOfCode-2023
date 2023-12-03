
digits = ['0','1','2','3','4','5','6','7','8','9']
allowed_neighbor_values = digits + ['.']

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
    posible_part_number = ''
    is_part_number = False
    for column_index in range(len(row)):
        if row[column_index] in digits:
            is_in_number = True
            posible_part_number += row[column_index]
            if has_disallowed_symbols_in_neighborhood(
                rows=rows,
                row_index=row_index,
                column_index=column_index,
                allowed_neighbor_values=allowed_neighbor_values
            ):
                is_part_number = True
            if is_part_number and column_index == (len(row) - 1):
                row_part_numbers.append(posible_part_number)
                cumulative_all_numbers += int(posible_part_number)

        else:
            if is_in_number:
                # we found the end of a number, add it to the list if it is a part number
                if is_part_number:
                    row_part_numbers.append(posible_part_number)
                else:
                    print(posible_part_number)
                cumulative_all_numbers += int(posible_part_number)
                posible_part_number = ''
                is_part_number = False
            is_in_number = False
    
    # print(row_part_numbers)
    for row_part_number in row_part_numbers:
        cumulative_part_numbers += int(row_part_number)
                

    row_index += 1

print(f"all: {cumulative_all_numbers}")
print(f"answer: {cumulative_part_numbers}")