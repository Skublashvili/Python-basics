year = int(input("Which year do you want to check? "))

if year % 4 != 0:
    print("Not leap")
else:
    if year % 100 != 0:
        print("Leap")
    else:
        if year % 400 != 0:
            print("Not leap")
        else:
            print("Leap")


