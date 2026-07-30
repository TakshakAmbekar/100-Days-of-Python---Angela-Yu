# Lists in python are equivalent of arrays in C++, but there can be elements with different datatypes

list = [1, "A", True]

print(list)

print(list[0])
print(list[-1])

list.append(1.0)    # Add a single element at the end
print(list)

list.extend([1, 2, 3])  # Add multiple elements or elements from another list at the end
print(list)



# Nested Lists
fruits = ["Apple", "Peach", "Banana"]
vegetables = ["Spinach", "Tomato", "Potato"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1][-1])
