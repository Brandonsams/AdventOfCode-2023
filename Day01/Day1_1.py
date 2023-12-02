digits = ['0','1','2','3','4','5','6','7','8','9']

cumulative_calibration_value = 0

with open("./Day01//Day1_1.txt") as f:
    for line in f.readlines():
        line = line.rstrip()
        line_length = len(line)

        first_digit = None
        last_digit = None
        calibration_value = 0

        # Find first digit in line
        for i in range(line_length):
            if line[i] in digits:
                first_digit = line[i]
                # print(f"found a first digit: {line[i]}")
                break

        # Find last digit in line
        for i in range(line_length):
            if line[line_length -1 - i] in digits:
                last_digit = line[line_length - 1 - i]
                # print(f"found a last digit: {line[line_length - 1 - i]}")
                break

        if first_digit == None:
            print("uh oh 1")

        if last_digit == None:
            print("uh oh 2")

        calibration_value = int(first_digit + last_digit)
        cumulative_calibration_value = cumulative_calibration_value + calibration_value
        
# 56397
print(cumulative_calibration_value)
