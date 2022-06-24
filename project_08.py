import os
def clear():
    os.system('clear') 

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

again = True
players = {}

def find_winner(biding):
    highest = 0
    winner = ""
    for bidder in biding:
        bid_amount = biding[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest}")

print(logo)
while again:
    name = input("What's your name? ")
    bid = int(input("What's your bid? "))
    players[name] = bid
    sim = input("There're others players? yes or no. ")
    if sim == "no":
        again = False
        clear()
        find_winner(players)
    else:
        clear()
        
    
        
    




