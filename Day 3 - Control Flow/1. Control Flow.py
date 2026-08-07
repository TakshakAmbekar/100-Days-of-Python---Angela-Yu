print("Welcome to the roller coaster!")

height = float(input("Enter your Height in cm:\n"))

total = 0

if height >= 120:
    age = int(input("Enter your Age:\n"))

    print("You can ride the roller coaster!")
    if age < 12:
        print("Child ticket price: $5")
        total = 5
    elif age < 18:
        print("Youth ticket price: $10")
        total = 10
    else:
        print("Adult ticket price: $15")
        total = 15

    wants_photo = input("Do you want a photograph? Enter y or n: ")
    if wants_photo == 'y':
        total += 3
        print("That will cost you an extra $3.")
    print(f"Your total is ${total}.")

else:
    print("Sorry, you are too short ride the roller coaster...")