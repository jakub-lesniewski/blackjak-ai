import random
from classes.card import Card, ranks, suits

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
    