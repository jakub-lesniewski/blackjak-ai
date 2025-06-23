import sys
from classes.deck import Deck
from classes.player import HumanPlayer
from classes.dealer import Dealer
from classes.ai_player import AIPlayer


def main():
    deck = Deck()
    deck.generate_deck()
    deck.shuffle_deck()

    player = HumanPlayer("Player")
    opponent = AIPlayer("Computer", simulations=10_000)
    dealer = Dealer()

    for _ in range(2):
        player.receive_card(deck.draw_card())
        opponent.receive_card(deck.draw_card())
        dealer.receive_card(deck.draw_card())

    dealer.show_up_card()
    player.show_hand()

    while True:
        action = player.decide()
        if action == "hit":
            player.receive_card(deck.draw_card())
            player.show_hand()
            if player.hand_value() > 21:
                print("You busted! Dealer and Computer win.")
                return 1
        else:
            print(f"{player.name} stands at {player.hand_value()}.")
            break

    print("\nComputer's turn:")
    opponent.show_hand()
    while True:
        decision = opponent.decide(deck, dealer.hand[0])
        print(f"Computer decides to {decision}.")
        if decision == "hit":
            opponent.receive_card(deck.draw_card())
            opponent.show_hand()
            if opponent.hand_value() > 21:
                print("Computer busted! You and Dealer win.")
                return 1
        else:
            print(f"Computer stands at {opponent.hand_value()}.")
            break

    print("\nDealer's turn:")
    dealer.show_hand()
    dealer_busted = False
    while dealer.decide() == "hit":
        print("Dealer hits.")
        dealer.receive_card(deck.draw_card())
        dealer.show_hand()
        if dealer.hand_value() > 21:
            print("Dealer busted!")
            dealer_busted = True
            break
    if not dealer_busted:
        print("Dealer stands at {0}.".format(dealer.hand_value()))

    player_total = player.hand_value()
    opponent_total = opponent.hand_value()
    dealer_total = dealer.hand_value()

    scores = {
        "Player": player_total,
        "Computer": opponent_total,
        "Dealer": dealer_total
    }
    for name, score in list(scores.items()):
        if score > 21:
            scores[name] = -1
    winner = max(scores, key=lambda name: scores[name])

    top_score = scores[winner]
    tied = [name for name, score in scores.items() if score == top_score]
    if top_score < 0:
        print("All players busted. No winners.")
    elif len(tied) == 1:
        print(f"Winner: {winner} with {top_score} points.")
    else:
        print(f"Tie between: {', '.join(tied)} with {top_score} points.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
