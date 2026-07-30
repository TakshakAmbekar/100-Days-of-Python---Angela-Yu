for i in range(1, 101):
    word = "" 
    if i % 3 == 0:
        word += "Fizz"
    if i % 5 == 0:
        word += "Buzz" 
    print(i, word)  