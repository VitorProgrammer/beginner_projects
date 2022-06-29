import random
import os

def clearConsole():
    command = 'clear'
    os.system(command)

def game():
    logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     
    print(logo)

    end_game = False
    want_more = True
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_cards = []
    dealer_cards = []
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))

    dealer_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

    user_hand_total = sum(user_cards)
    dealer_hand_total = sum(dealer_cards)
    
    print(f"Your cards are {user_cards}.")
    print(f"The first Dealer card is {dealer_cards[0]}.")

    while want_more is True: 
        if user_hand_total and dealer_hand_total == 21: 
            print(f"The dealer cards are: {dealer_cards}, the sum is {dealer_hand_total}. You Lose!")
            end_game = True
            want_more = False
            break
        elif dealer_hand_total == 21:
            print(f"The dealer cards are: {dealer_cards}, the sum is {dealer_hand_total}. You Lose!")
            end_game = True
            want_more = False
            break
        elif user_hand_total == 21:
            print(f"Your cards are: {user_cards}, the sum is {user_hand_total}. You Win!")
            end_game = True
            want_more = False
            break
        elif user_hand_total > 21:
            if(11 in user_cards):
                for number in user_cards:
                    if number == 11:
                        number = 1
                        print("Your ace now has a value of: 1")
            else:
                want_more = False
                break

        again_1 = input("\nDo you want another card? 'y' or 'n': ")

        if end_game == False:
            if again_1 == "n":
                while dealer_hand_total < 16:
                    dealer_cards.append(random.choice(cards))
                    dealer_hand_total = sum(dealer_cards)
                    if dealer_hand_total > 21:
                        if(11 in dealer_cards):
                            for number in user_cards:
                                if number == 11:
                                    number = 1
                                    print("Your ace now has a value of: 1")

                want_more = False
            elif again_1 == "y":    
                user_cards.append(random.choice(cards))
                print(f"Your cards are: {user_cards}.")
                
        user_hand_total = sum(user_cards)
        dealer_hand_total = sum(dealer_cards)

        if user_hand_total > 21:
            want_more = False
        
    if end_game == False:
        print(f"\nYour cards are {user_cards}. And the sum are {user_hand_total}!")
        print(f"The Dealer cards are {dealer_cards}. And the sum are: {dealer_hand_total}!\n")

        if user_hand_total > dealer_hand_total and user_hand_total <= 21:
            print("You Win!!!")
        elif user_hand_total == dealer_hand_total:
            print("It's a draw!!!")
        elif dealer_hand_total > 21:
            print("You Win!!!")
        else:
            print("You Lose!!!")
    
    new_game = input("\nDo you want to play a new game? 'y' or 'n': ")
    if new_game == "y":
        clearConsole()
        game()
    else:
        print("Have a nice dayyy!!!")

game()







