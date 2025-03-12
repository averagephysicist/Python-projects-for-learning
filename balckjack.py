import random
print("Welcome to the blackjack game!")

cards = {"A":1, "2": 2, "3": 3, "4": 4, "5": 5,"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J":10, "Q":10, "K":10}
player_hand = []
computers_hand = []

#Getting the cards for the dealer and the player
while len(player_hand) <= 1:
    player_hand.append(random.choice(list(cards.keys())))
    computers_hand.append(random.choice(list(cards.keys())))

print(f"Your hand: {player_hand}" )
print(f"Computers hand: [{computers_hand[0]}]")
#counting the score and handling the As
def score_counting(hand):
    total = sum(cards[card] for card in hand)
    if "A" in hand and total + 10 <= 21:
        total += 10
    return total    
print(f"Your score: {score_counting(player_hand)}")


#GamePlay
while True:
    
#Hit    
    choice = input("Press \'Y\' to hit. Press \'S\'  to stand \n").upper()
    if choice == "Y":
        player_hand.append(random.choice(list(cards.keys())))
        print(f"Your hand: {player_hand}")
        print(f"Your current score: {score_counting(player_hand)}")
        if score_counting(player_hand) > 21:
            print("Your score is more than 21. You lose!")
            break
        if score_counting(player_hand) == 21:
            print("Your score is 21. You win!")        

#Stand
    elif choice == "S":
        print(f" Computers hand: {computers_hand} ")
        print(f"Computer's count: {score_counting(computers_hand)}")

        if score_counting(computers_hand) == score_counting(player_hand) and score_counting(computers_hand)>= 17:
            print("It's a tie!")         

        while score_counting(computers_hand) < 17:
            computers_hand.append(random.choice(list(cards.keys())))
            print(f"computers hand: {computers_hand}")
            print(f"computers count: {score_counting(computers_hand)}")

            if score_counting(computers_hand) > 21:
                print("Dealer Busts, you win!")
                break
    
        if score_counting(computers_hand) > score_counting(player_hand) and score_counting(computers_hand)<= 21:
                print("Dealer wins! You lose")
               
        else: 
            print("Congratulations, you win!")   
            break 

        
            
    

      


    

