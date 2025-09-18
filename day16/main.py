from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# User input turn off by "off"
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True
while is_on:
    print(f"What would you like? {menu.get_items()}: ")
    coffee_choice = input().lower()
    if coffee_choice == "off":
        is_on = False
    elif coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
    # check if ordered drink is present in menu
    elif coffee_choice in menu.get_items().split("/"):
        menu_item = menu.find_drink(coffee_choice)
        print(f"You have ordered: {menu_item.name}")
        print(f"Ingredients needed {menu_item.ingredients}")

        if menu_item is not None:
            # check if resources are enough to give drink
            if coffee_maker.is_resource_sufficient(menu_item):
                if money_machine.make_payment(menu_item.cost):
                    coffee_maker.make_coffee(menu_item)

    else:
        menu_item = menu.find_drink(coffee_choice)
