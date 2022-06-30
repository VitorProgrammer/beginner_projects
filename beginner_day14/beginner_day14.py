import random
import os
from art import logo
from art import vs
from data import data

def clearConsole():
    command = 'clear'
    os.system(command)

def computer_choice():
    choice = random.choice(data)
    return choice


def game():
    end_game = False
    score = 0
    while end_game == False:
        if score == 0:
            choice_a = computer_choice()
        else:
            if a > b:
                choice_a = choice_a
            else:
                choice_a = choice_b

        choice_b = computer_choice()
        
        print(logo)
        print(f"\nCompare A: {choice_a['name']}, a {choice_a['description']} from {choice_a['country']}!!!" )

        print(vs)

        print(f"Against B: {choice_b['name']}, a {choice_b['description']} from {choice_b['country']}!!!")

        answer = input("Who has more followers? 'A' or 'B': ")
        a = choice_a['follower_count']
        b = choice_b['follower_count']

        if answer == "A" or answer == "a":
            if a > b:
                score += 1
                clearConsole()
                print(f"\nYou are rigth! Current score: {score}")
            else:
                print("You are wrong.")
                new_game = input("Do you want to play a new game? 'y' or 'n': ")
                if new_game == "y":
                    clearConsole()
                    game()
                else:    
                    end_game = True
        elif answer == "B" or answer == "b":
            if b > a:
                score += 1
                clearConsole()
                print(f"You are rigth! Current score: {score}")
            else:
                print("You are wrong.")
                new_game = input("Do you want to play a new game? 'y' or 'n': ")
                if new_game == "y":
                    clearConsole()
                    game()
                else:    
                    end_game = True
game()
