import random

BLACKJACK = 21
DEALER_STAND = 17
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(hand):
    """Deals one random card to a hand."""
    hand.append(random.choice(CARDS))


def score(hand):
    """Returns the best blackjack score for a hand."""
    total = sum(hand)
    aces = hand.count(11)

    while total > BLACKJACK and aces:
        total -= 10
        aces -= 1

    return total


def show_hand(name, hand, hide_second=False):
    if hide_second:
        print(f"{name}: [{hand[0]}, ?]")
    else:
        print(f"{name}: {hand} (Score: {score(hand)})")


def player_turn(player):
    while score(player) < BLACKJACK:
        choice = input("Draw another card? (y/n): ").lower()

        if choice != "y":
            break

        deal_card(player)
        print(f"You drew {player[-1]}")
        show_hand("Player", player)

    return score(player)


def dealer_turn(dealer):
    while score(dealer) < DEALER_STAND:
        deal_card(dealer)
        print(f"Dealer drew {dealer[-1]}")

    return score(dealer)


def determine_winner(player, dealer):
    player_score = score(player)
    dealer_score = score(dealer)

    if player_score > BLACKJACK:
        return "You Lost! You went over 21."

    if dealer_score > BLACKJACK:
        return "You Won! Dealer went over 21."

    if player_score > dealer_score:
        return "You Won!"

    if dealer_score > player_score:
        return "You Lost!"

    return "It's a Tie!"


def play_game():
    player = []
    dealer = []

    for _ in range(2):
        deal_card(player)
        deal_card(dealer)

    print("\n===== BLACKJACK =====\n")

    show_hand("Dealer", dealer, hide_second=True)
    show_hand("Player", player)

    if score(player) != BLACKJACK:
        player_turn(player)

    if score(player) <= BLACKJACK:
        dealer_turn(dealer)

    print("\nFinal Hands:")
    show_hand("Player", player)
    show_hand("Dealer", dealer)

    print("\n" + determine_winner(player, dealer))


if __name__ == "__main__":
    play_game()