
import random
import os

logo = """
 _   _                 _                 _____                     _              
| \ | |               | |               |  __ \                   (_)             
|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  \/_   _  ___  ___ ___ _ _ __   __ _  
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | __| | | |/ _ \/ __/ __| | '_ \ / _` | 
| |\  | |_| | | | | | | |_) |  __/ |    | |_\ \ |_| |  __/\__ \__ \ | | | | (_| | 
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|     \____/\__,_|\___||___/___/_|_| |_|\__, | 
                                                                            __/ | 
                                                                           |___/  
                                                                                                                                                                                    
"""
def clearConsole():
    command = 'clear'
    os.system(command)

def game():

    print(logo)

    numbers = []
    for n in range(1,101):
        numbers.append(n)

    key = random.choice(numbers)
    end_game = False

    def calculations():
        if guess - 20 > key:
            print("Too far away!!! it's a lot less!")
        elif guess + 20 < key:
            print("Too far away!!! it's a lot more!")
        elif guess > key:
            print("Too high!!!")
        elif guess < key:
            print("Too low!!!")
        else:
            print(f"Yahhh! You win, the correct number is {key}")
    while True:
        again = input("\nDo you want the 'hard' or 'easy' dificulty? ")
        if again == "hard":
            lives = 5
            print("Hard dificulty. You have 5 lives.")
            break
        elif again == "easy":
            lives = 10
            print("Easy dificulty. You have 10 lives.")
            break
        else:
            print("Invalid command.")


    while not end_game:
        guess = int(input("\nGuess a number between 1 and 100: "))
        calculations()
        if guess == key:
            new_game = input("\nDo you want to play a new game? 'y' or 'n': ")
            if new_game == "y":
                clearConsole()
                game()
            end_game = True
        elif guess != key:
            lives -= 1
            print(f"You have {lives} lives remainig.")
            if lives == 0:
                print("\nYou lost")
                end_game = True

game()