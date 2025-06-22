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
    "Queen": 10,
    "King":  10,
    "Ace":   11,
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

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card(rank={self.rank!r}, suit={self.suit!r})"

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