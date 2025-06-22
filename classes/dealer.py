from classes.player import HumanPlayer

class Dealer(HumanPlayer):
    def __init__(self, name="Dealer"):
        super().__init__(name)

    def show_up_card(self):
        """
        Reveal only the dealer's first card (the "up-card").
        """
        if not self.hand:
            print(f"{self.name} has no cards yet.")
        else:
            print(f"{self.name} shows: {self.hand[0]}")

    def decide(self):
        """
        Dealer must hit until reaching a hand value of at least 17.
        Returns 'hit' or 'stand'.
        """
        total = self.hand_value()
        # Standard: dealer stands on all 17s (hard or soft)
        if total < 17:
            return "hit"
        else:
            return "stand"
