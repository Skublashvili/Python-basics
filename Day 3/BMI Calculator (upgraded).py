height = float(input("Enter your height in M: "))
weight = float(input("Enter your weight in Kg: "))

bmi = round(weight / height ** 2, 1)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are slightly underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, your weight and height are in balance.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overrweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese, please take care of your health.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese, it would be good to go to the doctor.")