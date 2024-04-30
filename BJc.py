import random
import itertools

# Note: used Alphabets: i, z, x

# Deck of cards
deck = ((['A'])*4 + (list(range(2, 10)) * 4) + [10] * 16) * 6
random.shuffle(deck)

z = 0
for i in deck:
    if z % 52 == 0:
        print()
    print(i, end=',')
    z += 1


# Calculate cards value
def total(turn):
    total = 0
    ace_11s = 0
    for card in turn:
        if card in range(11):
            total += card
        else:
            total += 11
            ace_11s += 1
    while ace_11s and total > 21:
        total -= 10
        ace_11s -= 1
    return total


# Deal the cards
def dealCard(turn):
    card = deck[0]
    turn.append(card)
    deck.remove(card)


# Input
print("\n------------------------")
num_players = int(input("No. of players?: "))
table_rounds = int(input("Table rounds?: "))
# num_players = 3
# table_rounds = 2


# Playing against dealer card (2-to-6 And, rest)
x = 0
while x < table_rounds:
    direct_hands = []
    bjc = []
    players = [[] for i in range(num_players)]
    D = []
    for player in players:
        dealCard(player)
    dealCard(D)
    for player in players:
        dealCard(player)
        if total(player) == 21: # if total(player) == 21 and (D != 'A' and D != 10):
            bjc[:0] = player
            player.clear()
            tuple(player)
    if total(D) <= 6:
        for player in players:
            while total(player) <= 12 and type(player) != tuple:
                dealCard(player)
                if total(player) <= 21 and len(player) == 5:    # Cards5
                    direct_hands[:0] = player
                    player.clear()
                    player = tuple(player)
                elif total(player) >= 21 and len(player) > 2:  # sum21 & bust
                    direct_hands[:0] = player
                    player.clear()
                    player = tuple(player)
    else:
        for player in players:
            while total(player) < 17 and type(player) != tuple:
                dealCard(player)
                if total(player) <= 21 and len(player) == 5:
                    direct_hands[:0] = player
                    player.clear()
                    player = tuple(player)
                elif total(player) >= 21 and len(player) > 2:
                    direct_hands[:0] = player
                    player.clear()
                    player = tuple(player)
    while total(D) < 17 and len(players) > 0:
        dealCard(D)
    # sum21 = [player for player in players if total(player) == 21 and len(player) > 2]
    # bust = [player for player in players if total(player) > 21]
    # cards5 = [player for player in players if total(player) <= 21 and len(player) == 5]
    stay_hands = list(itertools.chain.from_iterable(reversed(players)))
    played_hands = D + stay_hands + direct_hands + bjc
    deck.extend(played_hands)
    x += 1

print("\n------------------------")
for i in range(num_players):
    print(f"P{i+1}: {players[i]} =\t{total(players[i])}")
print(f"D: {D} =\t{total(D)}")
print("-------------------------")
print("BJc = ", bjc)
print("direct_hands = ", direct_hands)
print("played_hands: ", played_hands)

# print(f"Final_deck: {deck}")    # Remaining + played cards
z = 0
for i in deck:
    if z % 52 == 0:
        print()
    print(i, end=',')
    z += 1
print("\n------------------------")
print("total_cards: ", len(deck))
