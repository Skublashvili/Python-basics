print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
a = name1.lower()
b = name2.lower()

count_number_1 = str(a.count("t") + a.count("r") + a.count("u") + a.count("e") + b.count("t") + b.count("r") + b.count("u") + b.count("e"))
count_number_2 = str(a.count("l") + a.count("o") + a.count("v") + a.count("e") + b.count("l") + b.count("o") + b.count("v") + b.count("e"))

score = int(count_number_1 + count_number_2)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
if score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
