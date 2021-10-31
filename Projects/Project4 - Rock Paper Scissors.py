import random

player_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choises = [rock, paper, scissors]
computer_choise = random.choice(choises)

if player_choise == 0:
    print("Your choise:\n" + rock)
    if computer_choise == rock:
        print("Computer choise:\n" + rock + "\nDraw!")
    elif computer_choise == paper:
        print("Computer choise:\n" + paper + "\nYou Lose!")
    else:
        print("Computer choise:\n" + scissors + "\nYou Win!")
elif player_choise == 1:
    print("Your choise:\n" + paper)
    if computer_choise == rock:
        print("Computer choise:\n" + rock + "\nYou Win!")
    elif computer_choise == paper:
        print("Computer choise:\n" + paper + "\nDraw!")
    else:
        print("Computer choise:\n" + scissors + "\nYou lose")
elif player_choise == 2:
    print("Your choise:\n" + scissors)
    if computer_choise == rock:
        print("Computer choise:\n" + rock + "\nYou Lose!")
    elif computer_choise == paper:
        print("Computer choise:\n" + paper + "\nYou Win!")
    else:
        print("Computer choise:\n" + scissors + "\nDraw!")
else:
    print("You typed an invalid number, you lose!")