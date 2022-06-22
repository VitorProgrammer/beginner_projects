import random
import os

def clear():
  os.system('clear') 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

word_list = [
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]

chosen_word = random.choice(word_list)

print(logo)

display = []
correct = []
lifes = 6

for _ in chosen_word:
    display += "_"
print(display)

for letter in chosen_word:
    correct += letter

lenght_word = len(chosen_word)

while display != correct: 
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}.\n")
    if guess not in correct:
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
    for position in range(lenght_word):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter 

    if guess in correct:
      print("Nice!\n")
    print(display)

    if display == correct:
        print(f"You win!\nThe word is {chosen_word}.")

    if guess in correct:
      print(f"{stages[lifes]}") 

    if guess not in correct:    
      lifes -= 1
      print(f"{stages[lifes]}")
      if lifes == 0:
        print(f"You lose!\nThe word is {chosen_word}.")
        break
