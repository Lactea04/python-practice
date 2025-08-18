import plotly.express as px

from die import Die

#make 6sides dice and 10sides dice
die_1 = Die()
die_2 = Die(10)

# roll the dice and save results in a list
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analyzing results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#data visualization
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x' : 'Result', 'y' : 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

#additional custom
fig.update_layout(xaxis_dtick=1) #x축 눈금 사이의거리 설정

fig.show()
#파일로 저장
#fig.write_html('dice_visual_d6d10.html')