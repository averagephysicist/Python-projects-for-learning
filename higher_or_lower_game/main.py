#higher or lower game
from instagram_followers import instagram_followers
import random


def options():
    name = random.choice(list(instagram_followers.keys()))
    description = instagram_followers[name]["description"]
    return name, description

print("Welcome to higher or lower!")
print("You have to guess who has more instagram followers!")

#selecting two random personalities from the dictionary
option_A, description_A = options()
option_B, description_B = options()

#making sure the two options are different
while option_A == option_B:
    option_B = options()
score = 0
#GamePlay
while True:
    print(f"Who has more followers? \n ")    
    print(f"A: {option_A} - {description_A}")
    print(f"B: {option_B} - {description_B}")


    choice = input("Type \'A\' or \'B\':").upper()
    #storing the highest number of followers
    followers_A = instagram_followers[option_A]["followers"]
    followers_B = instagram_followers[option_B]["followers"]

    #Determine the correct choice

    correct_choice = 'A' if followers_A > followers_B else 'B'

    if choice == correct_choice:
        score += 1
        print(f" Correct! {option_A if correct_choice == 'A' else option_B} has more followers")
        print(f"Your score: {score}")
        #The correct choice becomes option A for next round
        (option_A, description_A) = (option_B, description_B) if correct_choice == 'B' else (option_A, description_A)
        option_B, description_B = options()
        while option_A == option_B:
            option_B = options()

    else: 
        print("You lose!")
        print(f"final score: {score}")  
        break      