height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

new_height = float(height)
new_weight = float(weight)

bmi = (new_weight / new_height ** 2)
new_bmi = round(bmi, 2)
print(new_bmi)