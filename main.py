# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
number_names = len(names)
random_choice = random.randint(0, number_names - 1)

person_pay = names[random_choice]

print(person_pay + " is going to pay for the meal. ")