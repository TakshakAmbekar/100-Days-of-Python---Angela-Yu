import random

BLACKJACK = 21
DEALER_STAND = 17


class Deck:
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def deal(self):
        return random.choice(self.cards)


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, deck):
        card = deck.deal()
        self.cards.append(card)
        return card

    @property
    def score(self):
        total = sum(self.cards)
        aces = self.cards.count(11)

        while total > BLACKJACK and aces:
            total -= 10
            aces -= 1

        return total

    @property
    def is_blackjack(self):
        return len(self.cards) == 2 and self.score == BLACKJACK

    @property
    def is_bust(self):
        return self.score > BLACKJACK


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Hand()
        self.dealer = Hand()

    def deal_initial_cards(self):
        for _ in range(2):
            self.player.add_card(self.deck)
            self.dealer.add_card(self.deck)

    def show_hands(self, reveal_dealer=False):
        print()

        if reveal_dealer:
            print(f"Dealer: {self.dealer.cards} (Score: {self.dealer.score})")
        else:
            print(f"Dealer: [{self.dealer.cards[0]}, ?]")

        print(f"Player: {self.player.cards} (Score: {self.player.score})")
        print()

    def player_turn(self):
        while not self.player.is_bust and self.player.score < BLACKJACK:
            choice = input("Draw another card? (y/n): ").lower()

            if choice != "y":
                break

            card = self.player.add_card(self.deck)
            print(f"\nYou drew {card}")
            self.show_hands()

    def dealer_turn(self):
        while self.dealer.score < DEALER_STAND:
            card = self.dealer.add_card(self.deck)
            print(f"Dealer drew {card}")

    def determine_winner(self):
        if self.player.is_bust:
            return "You Lost! You busted."

        if self.dealer.is_bust:
            return "You Won! Dealer busted."

        if self.player.is_blackjack and not self.dealer.is_blackjack:
            return "Blackjack! You Won!"

        if self.dealer.is_blackjack and not self.player.is_blackjack:
            return "Dealer has Blackjack! You Lost!"

        if self.player.score > self.dealer.score:
            return "You Won!"

        if self.player.score < self.dealer.score:
            return "You Lost!"

        return "It's a Tie!"

    def play(self):
        self.deal_initial_cards()

        print("\n========== BLACKJACK ==========")

        self.show_hands()

        self.player_turn()

        if not self.player.is_bust:
            self.dealer_turn()

        print("\nFinal Hands:")
        self.show_hands(reveal_dealer=True)

        print(self.determine_winner())


if __name__ == "__main__":
    game = BlackjackGame()
    game.play()