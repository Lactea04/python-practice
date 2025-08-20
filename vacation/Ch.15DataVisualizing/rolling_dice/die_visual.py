import plotly.express as px

from die import Die

#make 6sides dice
die = Die()

# roll the dice and save results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#analyzing results
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#data visualization
title = "Results of Rolling One D6 1,000 Times"
labels = {'x' : 'Result', 'y' : 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()