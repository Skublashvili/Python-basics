number = int(input("Which number do you want to check? "))

odd_even = (number % 2)

if odd_even == 1:
    print("This number is odd")
else:
    print("This number is even")