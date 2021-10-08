height = int(input("Welcome to the Rollercoaster, please enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the Rollercoaster!")
    age = int(input("Please enter your age: "))
    if age < 12:
        bill += 5
        print("Child tickets are 5$")
    elif age <= 18:
        bill += 7
        print("Youth tickets are 7$")
    elif age < 45 or age > 55:
        bill += 12
        print("Adult tickets are 12$")
        want_photos = input("Do you want to take a photo? Write Y or N: ")
        if want_photos == "Y":
            bill += 3
            print(f"The total bill is ${bill}")
    else:
        print("Today for you the Rollercoaster is free!")
else:
    print("Sorry, you need to grow to ride the Rollercoaster.")

    