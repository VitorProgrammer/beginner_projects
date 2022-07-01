MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
on = True


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def menu(choice):
    global money
    if choice == "espresso":
        if MENU[choice]["ingredients"]["water"] > resources["water"] or resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
            return False
        else:
            resources["water"] -= MENU[choice]["ingredients"]["water"]
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            money += MENU[choice]["cost"]
    else:
        if MENU[choice]["ingredients"]["water"] > resources["water"] or MENU[choice]["ingredients"]["milk"] > resources["milk"] or MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
            return False
        else:
            resources["water"] -= MENU[choice]["ingredients"]["water"]
            resources["milk"] -= MENU[choice]["ingredients"]["milk"]
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            money += MENU[choice]["cost"] 


def money_user(choice):
    quarters = int(input("\nHow many quarters(0.25)? ")) * 0.25
    dimes = int(input("How many dimes(0.10)? ")) * 0.10
    nickles = int(input("How many nickles(0.05)? ")) * 0.05
    pennies = int(input("How many pennies(0.01)? ")) * 0.01
    money_total = quarters + dimes + nickles + pennies
    if money_total < MENU[choice]["cost"]:
        return False
    else: 
        print(f"\nHere is ${money_total - MENU[choice]['cost']:.2f} in change.")


while on == True:
    user_choice = input("\nWhat would you like? (espresso / latte / cappuccino): " )

    if user_choice == "boss":
        print("\nHello Boss, you are in the mannager tools.")
        while True:
            boss_choice = int(input("\nWhat's your choice:\n1 - add 500ml water.\n2 - add 400ml milk\n3 - add 300g coffee.\n4 - View actual resources.\n5 - Turn the machine off for maintence.\n6 - Withdraw the money.\n7 - exit.\n"))
            
            if boss_choice == 1:
                resources["water"] += 500
                print(f"\nThe new resources are:")
                report()
            elif boss_choice == 2:
                resources["milk"] += 400
                print(f"\nThe new resources are:")
                report()
            elif boss_choice == 3:
                resources["coffee"] += 300
                print(f"\nThe new resources are:")
                report()
            elif boss_choice == 4:
                report()
            elif boss_choice == 5:
                on = False
                print("\nBye bye boss!")
                break
            elif boss_choice == 6:
                withdraw_money = float(input(f"Total money: {money}. How much do you want to withdraw?\n"))
                
                if withdraw_money > money:
                    print("\nNot enoght founds.\n")
                else:
                    money -= withdraw_money
                report()

            else:
                print("\nBye bye boss!")
                break

    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        print(f"\nPlease, insert the coins. The cost of the {user_choice} is ${MENU[user_choice]['cost']}.")
        
        if money_user(user_choice) == False:
            print("Sorry, you dont have enought money.")
        elif menu(user_choice) == False:
            print("\nSorry, not enought resources. Call the boss!")
            print("I'll return your money now.") 
        else:
            menu(user_choice) 
            print(f"Here is your {user_choice}, enjoy!")
            
    else:
        print("Invalid Command.")
        



