'''
Primitives: 
string - "Hello", "123", "3.14"
integer - 1, 0, -4
float - 3.14, -3.14
boolean - True and False
'''

variable = "abc"    # replace with different values to check the datatype using type() function
datatype = type(variable)
print(datatype)

# Type conversion
decimal = 3.14
print(int(decimal))

number = 3
print(float(number))

string = "123"
print(int(string) + 123)

print(str(decimal) + "abc")

zero = 0
print(bool(decimal))
print(bool(zero))