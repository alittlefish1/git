import csv
from matplotlib import pyplot as plt
from datetime import datetime

#从文件中获得日期及最高气温
#filename = 'sitka_weather_07-2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    #header_row = next(reader)
    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])

        except ValueError:
            print(row[0] + ' missing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor=(0.9,0.2,0.8),alpha=0.9)
plt.title("Daily high temperature,July 2014",fontsize=24)
plt.xlabel('',fontsize=4)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()

    #for index,column_header in enumerate(header_row):
      #  print(index,column_header)

