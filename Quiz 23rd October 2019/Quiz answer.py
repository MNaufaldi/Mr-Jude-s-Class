#%%
Part II
Number 1
a.  Parent = Spell
    Child = Accio(Spell), Confundo(Spell)
    
b.  Accio

c.  Error
d.  Error

#%%
#Number 2
from Classes import Staff
from Classes import Position
filename = "data.txt"

with open(filename) as file:
    test = file.readlines()
StaffList = {}    
#Setting up existing classes
for staff in test:
    try:
        staff = staff.split('#')
        staff[3] = staff[3].strip()
        staff[1] = Staff(staff[0],staff[1],staff[2],staff[3])
        StaffList[staff[0]] = staff[1]
    except IndexError:
        pass
condition = True

while condition:
    #Display
    for staff in StaffList.values():
        if len(staff.getName()) != 7:
            print("|{}\t|{}\t|{}{}\t|{}|".format(staff.getID(),staff.getName(),staff.getPosition(),' '*(7-len(staff.getName())),staff.getSalary()))
        else:
            print("|{}\t|{}\t|{}\t|{}|".format(staff.getID(),staff.getName(),staff.getPosition(),staff.getSalary()))
    print("1. New Staff\n2. Delete Staff\n3. View Summary Data\n4. Save and Exit")
    Choice = input("Input Choice:")
#--snip snip--#
#Add new Staff    
    if Choice == '1':
        #New Staff
        print("New Staff")
        conditionID = False
        conditionName = False
        conditionPos = False
        conditionSal = False
        
        while conditionID == False:
            ID = input("Input ID [SXXXX]:")
            if len(ID) != 5 or ID[0] != 'S' or (ID[1::].isdigit()) == False or ID in StaffList.keys():
                condition = False
            else:
                toAddID = ID
                conditionID = True
        
        
        while conditionName == False:
            Name = input("Input Name[0...20]:")
            if len(Name) <= 20:
                toAddName = Name
                conditionName = True
            else:
                pass
            
        
        while conditionPos == False:
            position = input("Input Position[Staff|Officer|Manager]:")
            if position not in ["Manager","Staff","Officer"]:
                pass
            else:
                toAddPosition = position
                conditionPos = True
        
        
        while conditionSal == False:
            Salary = input("Input Salary for {}:".format(toAddPosition))
            if toAddPosition == 'Manager' and int(Salary) > 10000000:
                toAddSalary = Salary
                conditionSal = True
            elif toAddPosition == 'Staff' and 3500000 < int(Salary) < 7000000:
                toAddSalary = Salary
                conditionSal = True
            elif toAddPosition == 'Officer' and 7000001 < int(Salary) < 10000000:
                toAddSalary = Salary
                conditionSal = True
        
        toAddName = Staff(toAddID,toAddName,toAddPosition,toAddSalary)
        StaffList[toAddID] = toAddName
#--snip snip--#
#Delete Staff
    elif Choice == '2':
        print("Delete Staff")
        toDeleteID = input("InputID[SXXXX]:")
        
        for IDs in StaffList.keys():
            if toDeleteID in IDs:
                del StaffList[toDeleteID]
                print("Data has been successfully deleted")
                break
            else:
                print("Not Found")
    
#--snip snip--#
#Salaries
    elif Choice == '3':
         Manager = []
         Officer = []
         staff = []
         for names in StaffList.values():
            #Check position
            if names.getPosition() == 'Manager':
                Manager.append(int(names.getSalary()))
            elif names.getPosition() == 'Officer':
                Officer.append(int(names.getSalary()))
            elif names.getPosition() == 'Staff':
                staff.append(int(names.getSalary()))
            #Calculate
            #Manager
         print("1. Manager\nMinimum Salary: {}\nMaximum Salary: {}\nAverage Salary: {}".format(
                min(Manager),
                max(Manager),
                sum(Manager)/len(Manager)))
            #Officer
         print("1. Manager\nMinimum Salary: {}\nMaximum Salary: {}\nAverage Salary: {}".format(
                min(Officer),
                max(Officer),
                sum(Officer)/len(Officer)))
            #Staff
         print("1. Manager\nMinimum Salary: {}\nMaximum Salary: {}\nAverage Salary: {}".format(
                min(staff),
                max(staff),
                sum(staff)/len(staff)))
        
    elif Choice == '4':
        print("Save and Exit")
        with open(filename,'w') as file:
            for IDs in StaffList.keys():
                ID = StaffList[IDs].getID()
                Name = StaffList[IDs].getName()
                position = StaffList[IDs].getPosition()
                Salary = StaffList[IDs].getSalary()
                file.write("{}#{}#{}#{}\n".format(ID,Name,position,Salary))
            condition = False
    elif Choice == '5':
        break

#%%