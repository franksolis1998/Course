from operator import truediv


MENU = {
    "espresso":{
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    # notifys if there is enough of one ingredient 
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry we don't have enough {item}")
            return False
    return True

def process_coins():
    # allows for money to be set up in the program
    print("Please insert your money.")
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many Dimes?: ")) * 0.10
    total += int(input("How many Nickles?: ")) * 0.05
    total += int(input("How many Pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_recived, drink_cost):
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost, 2)
        print(f"Here is ${change} in change. ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry you dont have enough money.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:  
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")



#todo 
is_on = True 

while True:
    choice = input("What would you like to order, (espresso/latte/capuccino)?: ")
    if choice == "off":
        is_on = False 
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
