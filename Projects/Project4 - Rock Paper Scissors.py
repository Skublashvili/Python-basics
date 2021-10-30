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
if player_choise == 0:
    print(rock)
elif player_choise == 1:
    print(paper)
else:
    print(scissors)



choises = [rock, paper, scissors]
computer_choise = random.choice(choises)