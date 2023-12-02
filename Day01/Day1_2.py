def split_string_by_reserved(input_string, reserved_list):
    result = []
    current_position = 0
    while current_position < len(input_string):
        found_reserved = False   
        for reserved_str in reserved_list:
            if input_string.startswith(reserved_str, current_position):
                result.append(reserved_str)
                # current_position += len(reserved_str)
                current_position += 1
                found_reserved = True
                break
        if not found_reserved:
            current_position += 1
    return result

digits = ['0','1','2','3','4','5','6','7','8','9','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digit_word_dict = {
    'one':'1',
    'two':'2', 
    'three':'3', 
    'four':'4', 
    'five':'5', 
    'six':'6', 
    'seven':'7', 
    'eight':'8', 
    'nine':'9'
}
cumulative_calibration_value = 0

fname = "./Day01/Day1_1.txt"
# fname = "./Day01/example.txt"
with open(fname) as f:
    for line in f.readlines():
        line = line.rstrip()
        line_length = len(line)

        first_digit = None
        last_digit = None
        calibration_value = 0

        digits_in_string = split_string_by_reserved(line, digits)

        # Find first digit in line
        first_digit = digits_in_string[0]
        if len(first_digit) > 1:
            first_digit = digit_word_dict[first_digit]


        # Find last digit in line
        last_digit = digits_in_string[-1]
        if len(last_digit) > 1:
            last_digit = digit_word_dict[last_digit]

        if first_digit == None:
            print("uh oh 1")

        if last_digit == None:
            print("uh oh 2")

        calibration_value = int(first_digit + last_digit)
        cumulative_calibration_value = cumulative_calibration_value + calibration_value
        
# 55701
print(cumulative_calibration_value)
