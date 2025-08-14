import matplotlib.pyplot as plt


#file_open
with open("kyong_gi_gwank_zu_weather_data.csv", "r") as f:
    data = f.readlines() #ex) '경기광주,2024-08-29 22:00,25.2\n'

with open("kyong_gi_gwank_zu_atmospheric_pressure.csv", "r") as f2:
    pressure_data = f2.readlines() #ex) '오포읍AWS(광주),2024-05-25 11:00,H,100715,100710,100720\n'
                                                                        # average,minimum,max


#data
x_values = []
y_values = []

x1_values = []
y1_values = []

#data_input
choose_data = input("\nPlease type the date which you want to see the temperature data "
                    "\nform yyyy-mm-dd:")

#distinguish_data
for datum in data[1:]:
    datum = datum.split(',')
    if choose_data in datum[1]:
        x_values.append(datum[1][11:])
        y_values.append(float(datum[2][:-1]))

for pressure_datum in pressure_data[1:]:
    pressure_datum = pressure_datum.split(',')
    if choose_data in pressure_datum[1]:
        if '양벌배수AWS(광주)' == pressure_datum[0]:
            x1_values.append(pressure_datum[1][11:])
            y1_values.append(float(pressure_datum[3]))


#data_visulization
plt.style.use('seaborn-v0_8-ticks')
fig, ax = plt.subplots(figsize=(10,6))

ax.plot(x_values, y_values, color='blue', linewidth=2)
ax.set_title(f"Temperature Data of Gwangju, Gyeonggi-do at {choose_data}", fontsize=10)
ax.set_xlabel("date-time", fontsize=10)
ax.set_ylabel("Temperature", fontsize=10)
ax.tick_params(labelsize=7)

ax2 = ax.twinx()
ax2.plot(x1_values, y1_values, color='red', linewidth=2)
ax2.set_ylabel("Atmosphere_Pressure", fontsize=10)


#show_graph
fig.tight_layout()
plt.show()




