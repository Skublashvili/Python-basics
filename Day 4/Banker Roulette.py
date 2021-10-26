names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

import random
random_name = random.choice(names)
print(random_name)