import matplotlib.pyplot as plt

from die import Die


#dice
dice_1 = Die()

#roll the dice and save the data
results = [dice_1.roll() for result in range(10_000)]


#variables
num_dice = 1
max_num = dice_1.num_sides
x_values = list(range(num_dice, max_num+1))
y_values = [results.count(value) for value in range(1,7)]
colors = ['red', 'blue', 'green', 'orange', 'yellow', 'purple']

#data visualization
plt.style.use("seaborn-v0_8-notebook")
fig, dice = plt.subplots(figsize=(10,6))
dice.bar(x_values, y_values, color=colors)


#graph customizing
dice.set_title("Results of a D6 10,000 times")
dice.set_xlabel("Result")
dice.set_ylabel("Frequency of result")

plt.show()

