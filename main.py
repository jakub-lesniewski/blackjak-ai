import random

ranks = {
    2:  1,
    3:  2,
    4:  3,
    5:  4,
    6:  5,
    7:  6,
    8:  7,
    9:  8,
    10: 9,
    "Jack":  10,
    "Queen": 11,
    "King":  12,
    "Ace":   13,
}

suits = [
    "Clubs",
    "Diamonds",
    "Hearts",
    "Spades"
]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def print_card(self):
        print(f"{self.rank} of {self.suit}")

    def __eq__(self, card):
        return ranks[self.rank] == ranks[card.rank]
    
    def __lt__(self, card):
        return ranks[self.rank] < ranks[card.rank]
    
    def __gt__(self, card):
        return ranks[self.rank] >  ranks[card.rank]
    
    def __le__(self, card):
        return ranks[self.rank] <=  ranks[card.rank]
    
    def __ge__(self, card):
        return ranks[self.rank] >=  ranks[card.rank]
    
class Deck:
    def __init__(self, cards=[]):
        self.cards = cards

    def generate_deck(self):
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))
    
    def print_deck(self):
        for index, card in enumerate(self.cards, start=1):
            print(index, end=". ")
            card.print_card()
    
    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

d1 = Deck()
d1.generate_deck()
c1 = d1.draw_card()
c1.print_card()
