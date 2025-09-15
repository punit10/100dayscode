import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 50
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "milk": 200,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 150,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 30,
    }
}

resources = {"water": 400, "milk": 400, "coffee": 100, "money": 0, "profit": 0}


def show_report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Profit: Rs. {resources['profit']}")
    print("Money left is {} Rs".format(resources['money']))


def is_sufficient_resources(drink):
    if resources['water'] < drink['ingredients']['water']:
        print("Sorry! not enough water!")
        return False
    elif resources['coffee'] < drink['ingredients']['coffee']:
        print("Sorry! not enough coffee!")
        return False
    elif resources['water'] < drink['ingredients']['water']:
        print("Sorry! not enough water!")
        return False
    else:
        return True


def is_money_processed(resources, money):
    resources['money'] += money
    print(f"money left {resources['money']}")
    if money < resources['money']:
        print("Sorry that's not enough money. Money refunded!")
        return False
    else:
        return True


def process_coffee(resources, drink):
    print(f"Preparing your {choice} Please wait...")
    time.sleep(3)
    resources['water'] -= drink['ingredients']['water']
    resources['coffee'] -= drink['ingredients'][
        'coffee']
    resources['money'] -= drink['cost']
    resources['profit'] += drink['cost']
    print(f"Here is your {choice}. Enjoy!!!")
    print(f"Here is your change refunded! {resources['money']} Rs")


is_on = True
while is_on:
    print("'off' to close, 'rep' to report")
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report" or choice == "rep":
        show_report()
    else:
        if choice == "espresso" or choice == "latte" or choice == "cappuccino":
            drink = MENU[choice]
            if is_sufficient_resources(drink):
                input_money = int(input("Pay money: "))
                if is_money_processed(resources, input_money):
                    process_coffee(resources, drink)
        else:
            print("Please choose correct option!")
