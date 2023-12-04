cards = {
    1: 5,
    2: 0
}

cards = {
    
}

points = 0

fname = "./Day04/input.txt"
# fname = "./Day04/example.txt"

original_card_count = len(list(open(fname)))
for card in range(original_card_count):
    cards[card + 1] = 1

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

        for won_copy in range(matched_number_count):
            try:
                cards[card + won_copy + 1] = cards[card + won_copy + 1] + cards[card]
            except:
                print("something went wrong")
            
        
        # points += score

        # print(f"Card {card}: {score} points")

        card += 1

card_count = 0
for card in cards:
    card_count += cards[card]

print(f"Total card: {card_count}")