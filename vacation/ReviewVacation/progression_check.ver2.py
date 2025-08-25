import csv
from pathlib import Path
import pandas as pd
from datetime import datetime

import plotly.express as px


#data
progression_data = [0, 0, 0, 1, 50, 48, 50]

excel_path = Path("C:\\Users\\kimtg\\OneDrive\\Desktop\\vacation\\vacation_plan_progress_file.xlsx")
df = pd.read_excel(excel_path)
df_csv = df.to_csv(index=False)
vacation_data = df_csv.splitlines() #'DATE,PLAN,PRG_PLAN,NUM_PLAN,NUM_PRG'
reader = csv.reader(vacation_data)
next(reader)

dates, nums_plan, nums_prg = [], [], []
#data separating
for row in reader:
    date = datetime.strptime(row[0], "%Y-%m-%d")
    dates.append(date)
    nums_plan.append(int(row[3]))
    nums_prg.append(int(row[4]))



#evaluation of Vacation plan's progression
def show_average(data):
    average = sum(data)/len(data)
    print(f"The average of Vacation_progression is {round(average)}%")
show_average(progression_data) #21%


#visualization
df1 = pd.DataFrame({
    "date" : dates,
    "progression" : nums_prg
})
df1["month"] = pd.to_datetime(df1["date"]).dt.strftime("%Y-%m")
fig = px.bar(df1, x="date", y="progression", title="날짜별 계획 이행 정도", color="month")

fig.show()