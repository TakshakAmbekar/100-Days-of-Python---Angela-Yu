# BMI equals weight in kg divided by square of height in m

height = float(input("Enter your height in cm\n"))
height /= 100

weight = float(input("Enter you weight in kg\n"))

bmi = weight / (height ** 2)

print(f"Your BMI is {round(bmi, 2)}")

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have a normal weight")
else:
    print("You are overweight")

