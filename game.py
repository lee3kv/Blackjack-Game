import random

# BLACKJACK
# My goal with this project is to find out a method for consistently winning in blackjack.
# I'll have 3 types of players: Myself (the control), a card counting bot, and a machine learning bot.
# Just like in standard casinos, the table will have 6 decks (totaling 52 * 6 = 312 cards), and will
# hit until reaching 17 or over. Aces still run as a 1 or 11, and the players options are limited to
# just hitting or standing (for simplicity sake).

# Global Variables
deck_size = 312 # Size of the large deck (6 decks)
ordered_deck = [] # The full stack of cards variable
shuffled_deck = [] # Variable to carry the shuffled values
tracker = 0 # Keep track of the position in the shuffled deck
dealer = [] # Dealer array
player = [] # Player array

# Class to make the stack of cards being used (in this case 6 decks)
class Card:
    # Constructor
    def __init__(self):
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.suits = ['S', 'D', 'C', 'H']

    # Create one deck, in order
    def Construct(self):
        for s in range(self.suit_len):
           for v in range(self.value_len):
                ordered_deck.append(self.values[v] + self.suits[s])
                shuffled_deck.append(self.values[v] + self.suits[s])

# Class to pull and keep track of the 6 decks
class Shuffler:
    # Similar to the machines in casinos, this will shuffle the 6 decks once the entire deck reaches 2
    # decks (104 cards) left.
    def Shuffle(self):
        global tracker
        random.shuffle(shuffled_deck)
        tracker = 0

    def Deal(self):
        global tracker
        for t in range(2):
            player.append(shuffled_deck[tracker])
            dealer.append(shuffled_deck[tracker+1])
            tracker += 2

    def Hit(self, person):
        global tracker
        person.append(shuffled_deck[tracker])
        tracker += 1

    def Show(self):
        global tracker
        print()


deck = Card()
shoe = Shuffler()

# Building an ordered deck
for i in range(6):
    deck.Construct()
print(ordered_deck)

# Shuffle if the total deck reaches the 4th deck
if tracker == 208:
    shoe.Shuffle()


shoe.Shuffle()
print(shuffled_deck)

shoe.Deal()
print(str(player) + ", " + str(dealer))
print(tracker)

if int(player[0][0]) + int(player[0][1]) < 21:
    shoe.Hit(player)
    print(str(player) + ", " + str(dealer))

shoe.Shuffle()
print(shuffled_deck)
print(tracker)