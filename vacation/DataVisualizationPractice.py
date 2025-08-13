import matplotlib.pyplot as plt


#file_open
with open("kyong_gi_gwank_zu_weather_data.csv", "r") as f:
    data = f.readlines() #ex) '경기광주,2024-08-29 22:00,25.2\n'

#data
x_values = []
y_values = []

#data_input
choose_data = input("\nPlease type the date which you want to see the temperature data "
                    "\nform yyyy-mm-dd:")

#distinguish_data
for datum in data[1:]:
    datum = datum.split(',')
    if choose_data in datum[1]:
        x_values.append(datum[1][11:])
        y_values.append(float(datum[2][:-1]))

#data_visulization
plt.style.use('seaborn-v0_8-talk')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, color='blue', linewidth=2)
ax.set_title(f"Temperature Data of Gwangju, Gyeonggi-do at {choose_data}", fontsize=10)
ax.set_xlabel("date-time", fontsize=10)
ax.set_ylabel("Temperature", fontsize=10)
ax.tick_params(labelsize=7)

#show_graph
plt.show()




