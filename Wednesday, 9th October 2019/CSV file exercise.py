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
                #date = datetime.strptime(row[1], "%Y-%m-%d")
            else:
                current_step.append(int(row[0]))
                allstep.append(int(row[0]))
                #date = datetime.strptime(row[1], "%Y-%m-%d")
plt.bar(range(1,61),totalstep)
plt.show()
print("Median: ",np.median(totalstep))
print("Mean: ",np.mean(totalstep))

#%%
#5 Minute pattern
import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = "activity.csv"
last_i = 0
step5 = []
datep = []
count = -5
av = []
avstep = []
average = 0
with open(filename) as w:
    reader = csv.reader(w)
    header = next(reader)
    for row in reader:
        if int(row[2]) - count == 5:
            if row[0] == 'NA':
                step5.append(0)
                date = datetime.strptime(row[1], "%Y-%m-%d")
                datep.append(date)
                count += 5
            else:
                step5.append(int(row[0]))
                date = datetime.strptime(row[1], "%Y-%m-%d")
                datep.append(date)
                count += 5
                average+=(int(row[0]))
        else:#Interval is more than 5 minute 
            times = int((int(row[2]) - count)/5)
            for num in range(times):
                if row[0] == 'NA':
                    step5.append(0)
                    date = datetime.strptime(row[1], "%Y-%m-%d")
                    count += 5
                    datep.append(date)
                else:
                    step5.append(int(int(row[0])/5))
                    date = datetime.strptime(row[1], "%Y-%m-%d")
                    datep.append(date)
                    count += 5
                    average+=(int(row[0]))
        if count == 2355:
            count = -5
            av.append(average/(2355/5))
            average = 0
#Im assuming the question A is average / 1 minute for the (x axis)
#I dont understand the question...
#And i dont understand why it turned into a bar chart... im sorry
            
plt.plot(step5,c="orange")
          

#%%
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
                NAcount +=1
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
                NAcount +=1
                #date = datetime.strptime(row[1], "%Y-%m-%d")
plt.bar(range(1,61),totalstep)
plt.show()
print("Median: ",np.median(totalstep))
print("Mean: ",np.mean(totalstep))
print("You have",NAcount,"missing data")
#I replaced the missing data with 0 but it can be modified from the code
#It could work with a data using a newly added list of data if i tweak the code a little bit
#%%
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
        
                    
                    
        if count == 2355:
            count = -5
            countday += 1
            time +=1
        
plt.plot(timekeepd,weekday,c='orange',alpha=0.7)
plt.plot(timekeepe,weekend,c='blue',alpha=0.5)                    
plt.show()

##For some reason it turned into bar chart... im sorry i dont understand












#%%
