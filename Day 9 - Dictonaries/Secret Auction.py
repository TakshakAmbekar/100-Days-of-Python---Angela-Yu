import os

bids = {}

more_bidders = True

while more_bidders:
    os.system('cls')
    print("Welcome to the secret auction program.")

    name = input("What is your name?\n")
    bid = int(input("Enter your bid:\n"))
    bids[name] = bid
    
    more_bidders = input("Are there any other bidders? y or n:\n") == 'y'
    
max_bid = 0
winner = ""

for bidder in bids:
    if bids[bidder] > max_bid:
        winner = bidder
        max_bid = bid[winner]
        
os.system('cls')
print(f"Winner is {winner} with a bid ${max_bid}")


