from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os, time


def clear():
    os.system('cls' if os.name == "nt" else "clear")
    

def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    is_on = True
    while is_on:
        clear()
        # greet the customer
        print("Welcome")
        
        # show the menu
        print("Menu:", menu.get_items())

        # take the order
        order = input("What would you like?\n")
        
        if order == "report":
            coffee_maker.report()
            money_machine.report()
        elif order == "off":
            is_on = False
            print("Turning the machine OFF...")
        elif menu.find_drink(order):
            drink = menu.find_drink(order)
            if coffee_maker.is_resource_sufficient(drink):
                price = drink.cost
                if money_machine.make_payment(price):
                    coffee_maker.make_coffee(drink)
                else:
                    break
        
        time.sleep(3)
        clear()


if __name__ == "__main__":
    main()