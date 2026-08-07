from requirements import MENU, COINS, resources
import time, os


def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
    
def divider(text=""):
    line = "=" * 50

    if text:
        print(f"{line} {text}")
    else:
        print(line)

def get_integer(prompt, start = 0, end = 100):
    print(prompt)
    while True:
        try:
            user_input = int(input(f"Enter a number between {start} and {end}: "))
            if start <= user_input <= end:
                return user_input
            print("\rYou entered a number out of range.")
        except ValueError:
            print("\rYou entered an invalid number.")


def coffee_type():
    '''Let the user decide the type of coffee'''
    clear()
    print("Our Menu:")
    coffees = list(MENU.keys())

    for i, coffee in enumerate(coffees, start=1):
        print(f"{i}. {coffee}")
    divider()
    print()
    
    choice = get_integer("Choose a coffee -> ", 1, len(coffees))
    print()

    return coffees[choice - 1]
    

def check_resources(coffee):
    '''Check if the machine has enough resources'''
    clear()
    coffee_ingredients = MENU[coffee]["ingredients"]
    for ingredient in coffee_ingredients:
        if resources[ingredient]["quantity"] < coffee_ingredients[ingredient]:
            print(f"\nSorry, there isn't enough {ingredient} for the {coffee}.")
            return False
    print(f"Yes, I can make one {coffee}.\n")
    return True
        
        
def check_money(coffee):
    '''Check if the money user has given is enough'''
    price = MENU[coffee]["price"]
    amount = 0
    
    for coin in COINS:
        if coin != "penny":
            number_of_coins = get_integer(f"{coin}s -> ")
        else:
            number_of_coins = get_integer(f"pennies -> ")
        amount += number_of_coins * COINS[coin]
        print()
    
    return amount, price
    
    
def complete_transaction(coffee):
    '''Update resources and serve the coffee'''
    coffee_ingredients = MENU[coffee]["ingredients"]
    price = MENU[coffee]["price"]
    
    for ingredient in coffee_ingredients:
        resources[ingredient]["quantity"] -= coffee_ingredients[ingredient]
    resources["money"]["quantity"] += price
    
    print(f"Here's your {coffee}. Enjoy!\n")


def greet():
    print("Welcome to Coffee Machine!\n")
    
    
def single_order():
    '''Take a single order'''
    coffee = coffee_type()
    
    enough_resources = check_resources(coffee)
    
    if not enough_resources:
        return False
    
    amount, price = check_money(coffee)
    clear()
    
    if amount >= price:
        print(f"Sufficient funds.\nEntered: ${amount:.2f}, Required: ${price:.2f}")
        if amount > price:
            print(f"Here's your change: ${amount - price :.2f}")
        complete_transaction(coffee)
        return True
    else:
        print(f"Insufficient funds for {coffee}.\nEntered: ${amount:.2f}, Required: ${price:.2f}\nMoney refunded.\n")
        return False


def report():
    clear()
    for resource, details in resources.items():
        if resource == "money":
            print(f"{resource}: {details['unit']}{details['quantity']:.2f}")
        else:
            print(f"{resource}: {details['quantity']} {details['unit']}")
    
    divider("Report")
    print()


def cancel_order():
    print("Order Cancelled\n")    


def turn_off():
    print("Turning the Coffee Machine OFF...\n")


def get_operations(OPERATIONS):
    operations = list(OPERATIONS.keys())
    print("Select an operation:")
    for i, operation in enumerate(operations, start=1):
        print(f"{i}. {OPERATIONS[operation]}")
        
    return operations
    

def choose_operation(prompt, op_list):
    op_num = get_integer(prompt, 1, len(op_list))
    return op_num


OPERATIONS = {
    single_order: "Place an order",
    report: "Get resource report",
    turn_off: "Turn the machine OFF"
}

    
def main():
    clear()
    greet()
    
    while True:
        operations = get_operations(OPERATIONS)  
        choice = choose_operation("", operations)
        print()
        operation = operations[choice - 1]
        result = operation()
        
        if operation is single_order:
            if not result:
                cancel_order()
            
            divider()
            frames = ["", ".", "..", "..."]

            for i in range(12):
                print(f"\rPreparing for next customer{frames[i % 4]:<3}", end="", flush=True)
                time.sleep(0.4)

            os.system("cls")
        if operation is turn_off:
            return

        
    
    
if __name__ == "__main__":
    main()