#Hangaman
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random

word_list = ["chamel", "rainbow", "lion", "king", "safari", "cloud", "day", "horizon", "rock", "paper", "scissors"]



while True:
    chosen_word = random.choice(word_list)
    number_attempts = 6

    print("Welcome to Hangman!")
    print(chosen_word)

   
    display = ["_" for _ in chosen_word]
    
    guessed_letters = set()


    while "_" in display and number_attempts > 0:
        #shows the current status
        print(stages[6-number_attempts])   
        print("\n" + " ".join(display))
       
        guess = input("Type in a letter:").lower()
        
        if len(guess) != 1:
            print("Please type in a single letter")
            continue

        if guess in guessed_letters:
            print("You have already picked this letter")
            continue
        guessed_letters.add(guess)
            
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if guess == letter:
                    display[index] = guess      

        else: 
            number_attempts -= 1
            
            print(f" Wrong guess! Number of attempts = {number_attempts}")
            
     
                
    if "_" not in display:
        print("Congratulations, You win!")
        break

    if number_attempts == 0:
        print("You lost. Game Over!")
        break
    
        