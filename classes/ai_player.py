import random
import copy
from classes.player import HumanPlayer

class AIPlayer(HumanPlayer):
    def __init__(self, name="AI", simulations=500):
        super().__init__(name)
        self.simulations = simulations

    def decide(self, deck, dealer_up_card):
        def simulate_action(action):
            wins = 0

            for _ in range(self.simulations):
                sim_deck_cards = deck.cards[:]
                random.shuffle(sim_deck_cards)

                sim_player = copy.deepcopy(self.hand)
                sim_dealer = [dealer_up_card]
                sim_dealer.append(sim_deck_cards.pop())

                if action == "hit":
                    sim_player.append(sim_deck_cards.pop())
                    if self._hand_value(sim_player) > 21:
                        continue

                while True:
                    dval = self._hand_value(sim_dealer)
                    if dval < 17:
                        sim_dealer.append(sim_deck_cards.pop())
                    else:
                        break

                pval = self._hand_value(sim_player)
                dval = self._hand_value(sim_dealer)

                if pval <= 21 and (dval > 21 or pval > dval):
                    wins += 1

            return wins / self.simulations

        stand_winrate = simulate_action("stand")
        hit_winrate = simulate_action("hit")

        return "hit" if hit_winrate > stand_winrate else "stand"

    @staticmethod
    def _hand_value(cards):
        total, aces = 0, 0
        for c in cards:
            if c.rank == "Ace":
                aces += 1
                total += 11
            elif isinstance(c.rank, int):
                total += c.rank
            else:
                total += 10
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total