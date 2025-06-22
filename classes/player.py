class HumanPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        print(f"\n{self.name}'s hand:")
        for card in self.hand:
            print(f" {card}")
        print(f"Total value: {self.hand_value()}\n")

    def hand_value(self):
        total = 0
        aces = 0

        for card in self.hand:
            if card.rank == "Ace":
                aces += 1
                total += 11
            elif isinstance(card.rank, int):
                total += card.rank
            else:
                total += 10

        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    def decide(self):
        valid = {"h": "hit", "hit": "hit", "s": "stand", "stand": "stand"}
        while True:
            choice = input(f"{self.name}, do you want to [H]it or [S]tand? ").strip().lower()
            if choice in valid:
                return valid[choice]
            print("Please enter ‘h’ (hit) or ‘s’ (stand).")
