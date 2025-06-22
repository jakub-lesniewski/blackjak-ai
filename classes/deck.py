import random
from classes.card import Card, ranks, suits

class Deck:
    def __init__(self, cards=None):
        self.cards = cards if cards is not None else []

    def generate_deck(self):
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))
    
    def print_deck(self):
        for idx, card in enumerate(self.cards, 1):
            print(f"{idx}. {card}")
    
    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()
    
    def __len__(self):
        return len(self.cards)

    def is_empty(self):
        return not self.cards
