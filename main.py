from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem  # Assuming you have a Menu class imported correctly

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True  # Initialize the loop control variable

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like: {options}")  # Fixed typo in the prompt
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None:  # Check if the drink exists in the menu
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
               coffee_maker.make_coffee(drink)
        else:
            print("Sorry, that item is not available. Please choose from the menu.")
