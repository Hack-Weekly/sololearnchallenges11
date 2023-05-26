VALUES = {"J": "11", "Q": "12", "K": "13", "A": "1"}
SUITS = ["H", "D", "C", "S"]

cards = input().split(' ')

cards = [f'{VALUES.get(card[0])}{card[1]}' if card[0] in VALUES else card for card in cards]
card_values = [int(card[:-1]) for card in cards]
max_of_a_kind = max(card_values.count(card_value) for card_value in card_values)
unique_card_count = len(set(card_values))
is_straight = sorted(card_values) == list(range(min(card_values), max(card_values) + 1))
is_flush = len({card[-1] for card in cards}) == 1

if is_straight and is_flush:
    if min(card_values) == 10:
        print('Royal Flush')
    else:
        print('Straight Flush')
elif is_straight:
    print('Straight')
elif is_flush:
    print('Flush')
elif max_of_a_kind == 4:
    print('Four of a Kind')
elif max_of_a_kind == 3:
    if unique_card_count == 2:
        print('Full House')
    else:
        print('Three of a Kind')
elif max_of_a_kind == 2:
    if unique_card_count == 4:
        print('One Pair')
    elif unique_card_count == 3:
        print('Two Pairs')
else:
    print('High Card')
