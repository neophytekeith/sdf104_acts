from random import *
names = input("Enter Names: ").split(",")
ran_index = randint(0, len(names) - 1)

print(f"{names[ran_index].title()} is going to buy the meal today!")
