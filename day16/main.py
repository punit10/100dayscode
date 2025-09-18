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
    choice = input().lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    # check if ordered drink is present in menu
    elif choice in menu.get_items().split("/"):
        chosen_item = menu.find_drink(choice)

        # check if resources are enough to give drink
        if coffee_maker.is_resource_sufficient(chosen_item):
            if money_machine.make_payment(chosen_item.cost):
                coffee_maker.make_coffee(chosen_item)

    else:
        menu_item = menu.find_drink(choice)
