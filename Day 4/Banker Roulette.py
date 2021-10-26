import random
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

#easier is to do it like this:
# random_name = random.choice(names)
# print(random_name)

random_name = random.randint(1, len(names)) - 1
print(names[random_name])