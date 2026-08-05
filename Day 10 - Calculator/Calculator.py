print("Welcome to the Calculator App\n")

stop = False

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

choice = 'n'

while not stop:
    if choice == 'n':
        first = float(input("First number:\n"))
    else:
        first = answer
    operation = input("\nPick an operation: + - * /\n")
    second = float(input("\nSecond number:\n"))
    
    if operation in operations.keys():        
        answer = operations[operation](first, second)
        print(f"\n{first} {operation} {second} = {answer}\n")
    else:
        print("\nSomething went wrong...\n")
    
    choice = input("Press enter to continue with current answer, press 'n' to start fresh, press 'q' to quit\n")
    
    if choice == 'q': stop = True

