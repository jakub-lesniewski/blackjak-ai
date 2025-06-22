from classes.deck import Deck
from classes.player import HumanPlayer
from classes.dealer import Dealer


def main():
    deck = Deck()
    deck.generate_deck()
    deck.shuffle_deck()

    player = HumanPlayer("Player")
    dealer = Dealer()

    for _ in range(2):
        player.receive_card(deck.draw_card())
        dealer.receive_card(deck.draw_card())

    # Show starting hands
    dealer.show_up_card()
    player.show_hand()

    # Player's turn
    while True:
        action = player.decide()
        if action == "hit":
            player.receive_card(deck.draw_card())
            player.show_hand()
            if player.hand_value() > 21:
                print("Bust! You lose.")
                return
        else:
            print(f"{player.name} stands at {player.hand_value()}.")
            break

    # Dealer's turn
    print("\nDealer's turn:")
    dealer.show_hand()
    while dealer.decide() == "hit":
        print("Dealer hits.")
        dealer.receive_card(deck.draw_card())
        dealer.show_hand()
        if dealer.hand_value() > 21:
            print("Dealer busts! You win.")
            return
    print("Dealer stands.")

    # Compare final totals
    player_total = player.hand_value()
    dealer_total = dealer.hand_value()
    print(f"\nFinal Totals - You: {player_total}, Dealer: {dealer_total}")
    if dealer_total > player_total:
        print("Dealer wins.")
    elif dealer_total < player_total:
        print("You win!")
    else:
        print("Push (tie).")


if __name__ == "__main__":
    main()
