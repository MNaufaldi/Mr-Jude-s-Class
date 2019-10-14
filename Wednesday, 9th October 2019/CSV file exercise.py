#%%
#Number 1
import matplotlib.pyplot as plt
import csv
import numpy as np
from datetime import datetime
filename = "activity.csv"
step = []
current_step = []
allstep = []
totalstep = []
date,datep = [],[]
NAcount = 0
with open (filename) as t:
    count = 0
    reader = csv.reader(t)
    header = next(reader)
    for row in reader:
        if count == 288:
            if row[0] != 'NA':
                current_step.append(int(row[0]))
                allstep.append(int(row[0]))
                date = datetime.strptime(row[1], "%Y-%m-%d")
                datep.append(date)
            totalstep.append(sum(current_step))
            step.append(current_step)
                
            
            current_step = []
            count = 0
        else:
            count += 1
            if row[0] != 'NA':
                current_step.append(int(row[0]))
                allstep.append(int(row[0]))
           
                
                #date = datetime.strptime(row[1], "%Y-%m-%d")
plt.hist(totalstep)
plt.title("Steps per day")
plt.xlabel("Steps")
plt.ylabel("Frequencies")
plt.show()
print("Median: ",np.median(sorted(totalstep)))
print("Mean: ",np.mean(totalstep))

#%%
#Number 2
#5 Minute pattern
import csv
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
filename = "activity.csv"
dict = {}
dictInterval = {}
dictIntervalWeekends = {}
dictIntervalWeekdays = {}

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        steps = row[0]
        if (steps != 'NA'):
            date = row[1]
            date2 = int (dt.datetime.strptime(date,"%Y-%m-%d").day)
            interval = int(row[2])
            
            dict.setdefault(str(date),[])
            dict[str(date)].append(int(steps))
            
            dictInterval.setdefault(interval,[])
            dictInterval[interval].append(int(steps))
            
            if (date2 % 7 == 0):
                dictIntervalWeekends.setdefault(interval,[])
                dictIntervalWeekends[interval].append(int(steps))
                
            else:
                dictIntervalWeekdays.setdefault(interval,[])
                dictIntervalWeekdays[interval].append(int(steps))
            
listDate,listTotal,listAve = [],[],[]
            
for i in dict.keys():
    listDate.append(i)
    listTotal.append(sum(dict.get(i)))
    listAve.append(np.mean(dict.get(i)))
averagePlot = []
averageInterval = []
for keys in dictInterval.keys():
    averagePlot.append(np.mean(dictInterval.get(keys)))
    averageInterval.append(keys)
plt.plot(averageInterval,averagePlot,c='orange')
plt.xlabel("Interval")
plt.ylabel("Average Steps")
plt.title("Average for each interval")
plt.show()
#%%
#Number 3
import matplotlib.pyplot as plt
import csv
import numpy as np
from datetime import datetime
filename = "activity.csv"
step = []
current_step = []
allstep = []
totalstep = []
date,datep = [],[]
NAcount = 0
with open (filename) as t:
    count = 0
    reader = csv.reader(t)
    header = next(reader)
    for row in reader:
        if count == 288:
            if row[0] == 'NA':
                current_step.append(0)
                allstep.append(0)
                date = datetime.strptime(row[1], "%Y-%m-%d")
                datep.append(date)
                NAcount +=1
            else:
                current_step.append(int(row[0]))
                allstep.append(int(row[0]))
                date = datetime.strptime(row[1], "%Y-%m-%d")
                datep.append(date)
                
            totalstep.append(sum(current_step))
            step.append(current_step)
            
            current_step = []
            count = 0
        else:
            count += 1
            if row[0] == 'NA':
                current_step.append(0)
                allstep.append(0)
                NAcount +=1
                #date = datetime.strptime(row[1], "%Y-%m-%d")
            else:
                current_step.append(int(row[0]))
                allstep.append(int(row[0]))
                
                #date = datetime.strptime(row[1], "%Y-%m-%d")
plt.hist(totalstep)
plt.title("Frequencies of Steps")
plt.xlabel("Steps")
plt.ylabel("Frequencies")
plt.show()
print("Median: ",np.median(sorted(totalstep)))
print("Mean: ",np.mean(totalstep))
print("You have",NAcount,"missing data that has been replaced with 0")
#I replaced the missing data with 0 but it can be modified from the code
#It could work with a data using a newly added list of data if i tweak the code a little bit
#%%
#Number 4 I have 2 answers
#Number 4A
#Activity patterns between weekdays and weekend
#Started from monday acc to data
import csv
import matplotlib.pyplot as plt
filename = "activity.csv"
weekday,weekend = [],[]
count = -5
time = 1
timekeepd,timekeepe = [],[]
countday = 0
totalstep = []
with open (filename) as t:
    reader = csv.reader(t)
    header = next(reader)
    for row in reader:
        if time == 8:#Reset
            time = 1
        if int(row[2]) - count == 5:#Interval 5 minute
            if row[0] == 'NA':
                if time  < 6:#Weekdays
                    weekday.append(0)
                    timekeepd.append(int(row[2])+(2355*countday))
                    count+=5
                    
                else:#Weekend
                    weekend.append(0)
                    timekeepe.append(int(row[2])+(2355*countday))
                    count+=5
                    
            else:
                if time  < 6:#Weekdays
                    weekday.append(int(row[0]))
                    timekeepd.append(int(row[2])+(2355*countday))
                    count+=5
                   
                else:#Weekend
                    weekend.append(int(row[0]))
                    timekeepe.append(int(row[2])+(2355*countday))
                    count+=5
                    
            
        else:#Interval is more than 5 minute 
            
            times = int((int(row[2]) - count)/5)
            for num in range(times):
                if row[0] == 'NA':
                    if time  < 6:#Weekdays
                        weekday.append(0)
                        timekeepd.append(int(row[2])+(2355*countday)+(num*5))
                        count+=5
                        
                    else:#Weekend
                        weekend.append(0)
                        timekeepe.append(int(row[2])+(2355*countday)+(num*5))
                        count+=5
                        
                else:
                    if time  < 6:#Weekdays
                        weekday.append(int(row[0]))
                        timekeepd.append(int(row[2])+(2355*countday)+(num*5))
                        count+=5
                        
                    else:#Weekend
                        weekend.append(int(row[0]))
                        timekeepe.append(int(row[2])+(2355*countday)+(num*5))
                        count+=5
        
                    
                    
        if count == 2355:#Reset per day
            count = -5
            countday += 1
            time +=1
        
plt.plot(timekeepd,weekday,c='orange',alpha=0.7)
plt.plot(timekeepe,weekend,c='blue',alpha=0.5) 
plt.title("Steps per 5 minutes throughout\n the weekdays and weekends")
plt.xlabel("5 Minute Interval")   
plt.ylabel("Steps")                
plt.show()

##For some reason it turned into bar chart... im sorry i dont understand
#%%
#Number 4B using Mr Jude's code
import csv
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
filename = "activity.csv"
dict = {}
dictInterval = {}
dictIntervalWeekends = {}
dictIntervalWeekdays = {}

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        steps = row[0]
        if (steps != 'NA'):
            date = row[1]
            date2 = int (dt.datetime.strptime(date,"%Y-%m-%d").day)
            interval = int(row[2])
            
            dict.setdefault(str(date),[])
            dict[str(date)].append(int(steps))
            
            dictInterval.setdefault(interval,[])
            dictInterval[interval].append(int(steps))
            
            if (date2 % 7 == 0) or (date2 % 6 == 0):
                dictIntervalWeekends.setdefault(interval,[])
                dictIntervalWeekends[interval].append(int(steps))
                
            else:
                dictIntervalWeekdays.setdefault(interval,[])
                dictIntervalWeekdays[interval].append(int(steps))
plotWeekdaysKeys,plotWeekdaysInterval = [],[]    
plotWeekendsKeys,plotWeekendsInterval = [],[]

for keys in dictIntervalWeekdays.keys():
    plotWeekdaysKeys.append(keys)
    plotWeekdaysInterval.append(np.mean(dictIntervalWeekdays.get(keys)))
    
for keys in dictIntervalWeekends.keys():
    plotWeekendsKeys.append(keys)
    plotWeekendsInterval.append(np.mean(dictIntervalWeekends.get(keys)))

plt.plot(plotWeekdaysKeys,plotWeekdaysInterval,c='blue',label='Weekday')
plt.plot(plotWeekendsKeys,plotWeekendsInterval,c='orange',label='Weekend')
plt.xlabel("Interval")
plt.ylabel("Average Steps")
plt.legend()










#%%