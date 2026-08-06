import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player = []
dealer = []

# deal to a person and increase their sum
def deal(person):
    person.append(random.choice(cards))

# deal the first 2 cards to player and dealer
for _ in range(2):
    deal(player)
    deal(dealer)
    

print("===============================Welcome to BlackJack===============================")

# print the initial hand
print(f"Your Cards: {player}")
print(f"Dealer's first card {dealer[0]}")

draw_more = True
game_over = False

# while player wants to draw more and his total is less than 21
while draw_more and not game_over:
    draw_more = input("Press 'y' to draw more, 'n' to stop.\n").lower() == 'y'
    if draw_more:
        deal(player)
        # display the latest card
        print(f"You were dealt {player[-1]}.")
        print(f"Your new hand: {player}, your score: {sum(player)}")
    
    # if player gets total > 21, he loses
    if sum(player) > 21:
        print("===============================You went over 21. You lose===============================")
        game_over = True 
    
    # if player gets total = 21, he wins
    if sum(player) == 21:
        print("===============================BlackJack!!! You win===============================")
        game_over = True
        
# if the player stops drawing before crossing 21
if not game_over:
    # if the dealer total is less than 17 then he must draw one more card
    if sum(dealer) < 17:
        print(f"Dealer's hand: {dealer}, Dealer's score: {sum(dealer)} < 17.")
        deal(dealer)
        print(f"The dealer was dealt {dealer[-1]}.")
        print(f"Dealer's new hand: {dealer}, Dealer's score: {sum(dealer)}.")
    
    # # display both totals
    # print(f"Dealer score: {sum(dealer)} and you have {sum(player)}.")
    
    # if dealer went over 21 or player has a total greater than dealer and less than 21
    if sum(dealer) > 21 or sum(player) > sum(dealer):
        print("===============================You win===============================")
    # if player and dealer have same total
    elif sum(player) == sum(dealer):
        print("===============================It's a draw===============================")
    # if player total is less than dealer
    else:
        # if there are 1 cards in player deck
        if 1 in player:
            for card in player:
                if card != 1:
                    continue
                
                # replace 1 with 11
                id = player.index(1)
                player[id] = 11
                                
                print(f"1 was transformed to 11.")
                print(f"Your new hand: {player}, your score: {sum(player)}")
                
                if sum(player) > sum(dealer) and sum(player) <= 21:
                    if sum(player) == 21:
                        print("BlackJack!!!")
                    print("===============================You win===============================")
                    # if there's a win, stop converting more 1s to 11s
                    break
                elif sum(player) == sum(dealer):
                    print("===============================It's a tie===============================")
                else:
                    print("===============================You lose===================================")
        else:            
            print("===============================You lose===============================")

print(f"player: {player}, dealer: {dealer}")
