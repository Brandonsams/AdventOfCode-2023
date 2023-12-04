
points = 0

fname = "./Day04/input.txt"
# fname = "./Day04/example.txt"
with open(fname) as f:
    card = 1
    for row in f.readlines():
        row = row.rstrip()
        data = row.split(":")[1]

        winning_number_data = data.split("|")[0]
        winning_numbers = winning_number_data.replace("  "," ").strip().split(" ")
        
        my_number_data = data.split("|")[1]
        my_numbers = my_number_data.replace("  "," ").strip().split(" ")

        matched_number_count = 0
        for my_number in my_numbers:
            if my_number in winning_numbers:
                matched_number_count += 1

        score = 0
        if matched_number_count > 0:
            score = pow(2, matched_number_count - 1)
        
        points += score

        print(f"Card {card}: {score} points")

        card += 1

print(f"Total points: {points}")