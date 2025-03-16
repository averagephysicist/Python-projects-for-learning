import random
number = random.randint(1, 100)
print(number)
#number gessing game


print("Welcome to the number guessing game! \n I am thinking a number between 1 and 100")

difficulty = input("Select the difficulty level: Type \' easy\' or \'hard\' \n").lower()

if difficulty == "easy":
    number_of_attempts = 10

elif difficulty == "hard":
    number_of_attempts = 5

while True:

    guess = int(input("type in your guess: \n"))





    if guess == number:
        print("Congratulations, you win!")
        break
    if guess != number:
        number_of_attempts -= 1       
        print(f"Remaining attempts: {number_of_attempts}") 
    
    if guess > number:
        print("Too high")
    if guess < number:
        print("Too low")    
    if number_of_attempts == 0:
        print("You Lose!")
        break
    

