from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path("weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
#['STATION', 'NAME', 'DATE', 'AWND', 'PGTM', 'PRCP', 'TAVG', 'TMAX',
# 'TMIN', 'WDF2', 'WDF5', 'WSF2', 'WSF5', 'WT01', 'WT02', 'WT04',
# 'WT05', 'WT08', 'WT09'] 0~18 PRCP:5

precipitations = []
dates = []

for row in reader:
    precipitation = float(row[5])
    date = datetime.strptime(row[2], "%Y-%m-%d")
    precipitations.append(precipitation)
    dates.append(date)

plt.style.use('seaborn-v0_8-bright')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, precipitations, color="blue")

title = "Daily Precipitation, 2021\nSitka"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=12)
ax.set_ylabel("Precipitation", fontsize=12)
ax.tick_params(labelsize=16)

plt.show()