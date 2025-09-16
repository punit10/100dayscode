from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# User input turn off by "off"
nescafe = CoffeeMaker()
nescafe_menu = Menu()
money = MoneyMachine()

state = True
while state:
    print("What would you like? (espresso/latte/cappuccino/): ")
    coffee_choice = input().lower()
    if coffee_choice == "off":
        state = False
    elif coffee_choice == "report":
        nescafe.report()
    # check if ordered drink is present in menu
    elif coffee_choice in nescafe_menu.get_items().split("/"):
        menu_item = nescafe_menu.find_drink(coffee_choice)
        print(f"You have ordered: {menu_item.name}")
        print(f"Ingredients needed {menu_item.ingredients}")

        if menu_item is not None:
            # check if resources are enough to give drink
            if nescafe.is_resource_sufficient(menu_item):
                if money.make_payment(menu_item.cost):
                    nescafe.make_coffee(menu_item)

    else:
        menu_item = nescafe_menu.find_drink(coffee_choice)