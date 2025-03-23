#Coffe machine project
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18, "milk": 0},
        "cost": 1.50
    },
    "latte": {
        "ingredients": {"water": 200, "coffee": 24, "milk": 150},
        "cost": 2.50
    },
    "cappuccino": {
        "ingredients": {"water": 250, "coffee": 24, "milk": 100},
        "cost": 3.50
    }
}

water = 1000
milk = 1000
coffee = 1000
money = 0
def making_coffee(order):
    global water, milk, coffee, money  #declare global to modify them inside the function

    if order not in MENU:
        return "Invalid choice, please type in a valid choice"
    
    ingredients = MENU[order]["ingredients"]

    #check if the ingredients left are enough 
    if water < ingredients["water"]:
        return " There is not enough water"
    if milk < ingredients["milk"]:
        return "There is not enough milk"
    if coffee < ingredients["coffee"]:
        return " There is not enough coffee"
    
    # deduct ingredients and adding the money
    water -= ingredients["water"]
    milk -= ingredients["milk"]
    coffee -= ingredients["coffee"]
    money += MENU[order]["cost"]
    return f"Here is your {order}"


def report():
    return f"Remaining resources: \n  water: {water}, coffee: {coffee}, milk {milk} \n current money: {money}"

#counting the money and returning change
def process_coins(order):
    
      
    dimes = 0.10
    quarters = 0.25
    nickles = 0.05
    pennies = 0.01
    cost = MENU[order]["cost"]

    print("Type in the amount of coins of each given type:")
    try:
        n_dimes = int(input("Type in the number of dimes "))
        n_quarters = int(input("Type in the number of quarters "))
        n_nickles = int(input("Type in the number of nickles "))
        n_pennies = int(input("Type in the number of pennies "))
    except ValueError:
        return  0, -1
    money_recieved = n_dimes*dimes + n_quarters*quarters + n_nickles* nickles + n_pennies * pennies
    

    if money_recieved >= MENU[order]["cost"]:
        change = money_recieved - MENU[order]["cost"]
        return money_recieved, change   

    
    else:
        return money_recieved, -1
    
    

while True:
    print("welcome to the coffee machine.")
    action = input(" What would you like?: latte, cappuccino, espresso (report/off)").lower()

    if action == "report":
        print(report())
    
    elif action in ("espresso", "latte", "cappuccino"):
       money_received, change = process_coins(action)
       if change >= 0:
           print(f"Money received: ${money_received:.2f}")
           print(f"Your change: ${change:.2f}")
           print(making_coffee(action))
       else: 
           print("Money insufficient")         
               
       
    elif action == "off":
        break
    else: 
        print("Please type in a valid choice") 