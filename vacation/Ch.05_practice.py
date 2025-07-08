import random

colors = ["red", "green", "yellow"]
alien_color = random.choice(colors)



if alien_color == "green":
   print("Player gets 5 points!")

elif alien_color == "red":
    print("Player gets 15 points!")
else:
    print("Player gets 10 points!")

age = random.choice(list(range(1,100)))

if age<2:
    print("baby")
elif age>=2 and age<4:
    print("toddler")
elif age>=4 and age<13:
    print("kid")
elif age>=13 and age<20:
    print("teenager")
elif age>=20 and age<65:
    print("adult")
else:
    print("elder")

fruits = ["apple", "cherry", "banana", "strawberry", "melon", "watermelon"]

FRUIT = []
for x in range(0,3):
    FRUIT.append(random.choice(fruits))

if "strawberry" in FRUIT:
    print("You do like strawberry!")
