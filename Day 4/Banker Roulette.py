import random
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

#easier is to do it like this:
# random_name = random.choice(names)
# print(random_name)

random_name = random.randint(0, len(names) - 1)
person_who_will_pay = (names[random_name])
print(person_who_will_pay + " will pay for a meal today.")