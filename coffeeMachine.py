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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is no sufficient {item}")
            return False
    return True


def process_coins():
    """Returns calculated amount"""
    total = int(input("how many quarters? : ")) * 0.25
    total += int(input("how many dimes? : ")) * 0.1
    total += int(input("how many nickles? : ")) * 0.05
    total += int(input("how many pennies? : ")) * 0.01
    return total


def is_transaction_successful(received_amount, drinks_cost):
    """if enough money received returns true else false"""
    if received_amount >= drinks_cost:
        global profit
        change = round(received_amount - drinks_cost, 2)
        print(f"here is your change {change}")
        profit += drinks_cost
        return True

    else:
        print("sorry paid amount is not enough.money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients :
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")


is_on = True
while is_on:
    choice = input("what would you like ? espresso, latte, cappuccino : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water : {resources['water']}")
        print(f"milk : {resources['milk']}")
        print(f"coffee : {resources['coffee']}")
        print(f"money : {profit}")
    else:
        drink = MENU[choice]
        if is_resource_enough(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
