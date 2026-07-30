print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n"))
percentage = float(input("What percentage of tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))

# rounding can skip trailing zeros and thus it won't always show 2 digits after decimal
contribution = round((bill * (1 + percentage / 100)) / people, 2)

# using :.2f in f-string converts the number into a string while keeping 2 decimals
print(f"Each person should pay: {contribution:.2f}")

