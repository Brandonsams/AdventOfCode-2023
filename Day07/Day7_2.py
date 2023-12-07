from enum import Enum
from tqdm import tqdm

cards_by_rank = ["A", "K", "Q", "T", "9",
                 "8", "7", "6", "5", "4", "3", "2", "J"]

HandType = Enum("HandType", [
    "Five_of_a_kind",
    "Four_of_a_kind",
    "Full_House",
    "Three_of_a_kind",
    "Two_pair",
    "One_pair",
    "High_card"
])


class CamelCardsHand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.card_counts = dict()
        for card in hand:
            self.card_counts[card] = self.card_counts.get(card, 0) + 1
        joker_bonus = self.card_counts.pop("J", 0)
        frequent_card = None
        # Special case handling for 5 Jokers
        if self.hand == "JJJJJ":
            self.card_counts["A"] = 0
        frequent_card = max(self.card_counts, key=self.card_counts.get)
        self.card_counts[frequent_card] += joker_bonus

    def get_hand_type(self):
        rv = None
        # "Five of a kind"
        if len(self.card_counts) == 1:
            rv = HandType.Five_of_a_kind
        # "Four of a kind"
        elif len(self.card_counts) == 2 and max(self.card_counts.values()) == 4:
            rv = HandType.Four_of_a_kind
        # "Full House"
        elif len(self.card_counts) == 2 and max(self.card_counts.values()) == 3:
            rv = HandType.Full_House
        # "Three of a kind"
        elif len(self.card_counts) == 3 and max(self.card_counts.values()) == 3:
            rv = HandType.Three_of_a_kind
        # "Two pair"
        elif len(self.card_counts) == 3 and max(self.card_counts.values()) == 2:
            rv = HandType.Two_pair
        # "One pair"
        elif len(self.card_counts) == 4 and max(self.card_counts.values()) == 2:
            rv = HandType.One_pair
        # "High card"
        else:
            rv = HandType.High_card
        return rv


def hand_a_better_than_hand_b(hand_a: CamelCardsHand, hand_b: CamelCardsHand) -> bool:
    if hand_a.get_hand_type().value < hand_b.get_hand_type().value:
        return True
    if hand_a.get_hand_type().value > hand_b.get_hand_type().value:
        return False

    for card_index in range(5):
        a_rank = cards_by_rank.index(hand_a.hand[card_index])
        b_rank = cards_by_rank.index(hand_b.hand[card_index])
        if a_rank < b_rank:
            return True
        if a_rank > b_rank:
            return False

    # They must be equal at this point, so a can't be strictly better than b
    return False


camel_cards_hands = []

fname = "./Day07/example.txt"
fname = "./Day07/input.txt"
with open(fname) as f:
    for line in tqdm(f.readlines()):
        line = line.rstrip()
        # print(line)
        hand = line.split()[0]
        bid = int(line.split()[1])
        new_camel_card_hand = CamelCardsHand(hand=hand, bid=bid)

        # Handle the first entry
        if len(camel_cards_hands) == 0:
            camel_cards_hands.append(new_camel_card_hand)
            continue

        # Insertion sort the rest
        for insertion_index in range(len(camel_cards_hands)):
            comparison_camel_card_hand = camel_cards_hands[insertion_index]

            if hand_a_better_than_hand_b(hand_a=new_camel_card_hand, hand_b=comparison_camel_card_hand):
                camel_cards_hands.insert(insertion_index, new_camel_card_hand)
                break
        else:
            camel_cards_hands.append(new_camel_card_hand)

answer = 0
rank = 1
for camel_cards_hand in camel_cards_hands[::-1]:
    answer += (camel_cards_hand.bid * rank)
    rank += 1

print(f"Answer: {answer}")
