rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

escolha = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
computador = random.randint(0, 2)

if escolha == 0 and computador == 0:
    print(rock)
    print("Computer choose:")
    print(rock)
    print("It's a draw!")
elif escolha == 1 and computador == 1:
    print(paper)
    print("Computer choose:")
    print(paper)
    print("It's a draw!")
elif escolha == 2 and computador == 2:
    print(scissors)
    print("Computer choose:")
    print(scissors)
    print("It's a draw!")
elif escolha == 0 and computador == 1:
    print(rock)
    print("Computer choose:")
    print(paper)
    print("You lose!")
elif escolha == 0 and computador == 2:
    print(rock)
    print("Computer choose:")
    print(scissors)
    print("You win!")
elif escolha == 1 and computador == 2:
    print(paper)
    print("Computer choose:")
    print(scissors)
    print("You lose!")
elif escolha == 1 and computador == 0:
    print(paper)
    print("Computer choose:")
    print(rock)
    print("You win!")
elif escolha == 2 and computador == 0:
    print(scissors)
    print("Computer choose:")
    print(rock)
    print("You lose!")
elif escolha == 2 and computador == 1:
    print(scissors)
    print("Computer choose:")
    print(paper)
    print("You win!")
else:
    print("Invalid number.")