'''
for item in list_of_items:
    do something to each item
'''

fruits = ["Apple", "Peach", "Banana"]
for fruit in fruits:
    print(fruit.upper())
    
    
# range function is exclusive of the stop parameter, with default start = 0 and default step = 1
for i in range(5):
    print(i)    
    
for i in range(10, 15):
    print(i)

for i in range(0, 50, 10):
    print(i)