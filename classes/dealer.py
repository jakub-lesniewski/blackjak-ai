from classes.player import HumanPlayer

class Dealer(HumanPlayer):
    def __init__(self, name="Dealer"):
        super().__init__(name)

    def show_up_card(self):
        if not self.hand:
            print(f"{self.name} has no cards yet.")
        else:
            print(f"{self.name} shows: {self.hand[0]}")

    def decide(self):
        total = self.hand_value()
        if total < 17:
            return "hit"
        else:
            return "stand"
