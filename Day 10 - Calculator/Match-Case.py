def calculate(first, second, operation):
    match operation:
        case '+':
            return first + second
        case '-':
            return first - second
        case '*':
            return first * second
        case '/':
            return first / second
        case _:
            return "Invalid operation"