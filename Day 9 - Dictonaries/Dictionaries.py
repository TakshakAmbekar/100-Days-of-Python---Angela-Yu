'''
key:value pairs
keys can be string or number
'''

colours = {
    "apple": "red",
    "peach": "green",
    "banana": "yellow"
}

print(colours)

print(colours.keys())       # returns a list of keys
print(colours.items())      # returns a list of key,value tuples

print(colours["peach"])
colours["peach"] = "pink"
print(colours["peach"])


for key in colours:
    print(f"{key}: {colours[key]}")
    

dict = {
    "a": 1,
    "b": 5,
    "c": 2
}

# finding the maximum value among the values
print(max(dict, key = dict.get))

