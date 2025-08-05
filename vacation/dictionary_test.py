
#alien
import random

aliens = []
colors = ["green", "yellow", "red", "blue"]
speed_levels = ["fast", "slow", "medium"]

for alien_number in range(30):
    new_alien = {}
    color = random.choice(colors)
    new_alien["color"] = color
    new_alien["points"] = random.choice(range(10))
    new_alien["speed"] = random.choice(speed_levels)
    aliens.append(new_alien)

for alien in aliens:
    print(alien)