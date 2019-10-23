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
filename = "data.txt"
dataList = []
with open(filename) as data:
    AllData = data.readlines()
    for data in AllData:
        dataList.append(data.replace('#',' '))
        dataDisplay = []
        dataDisplay.append(data.replace('#',' '))
        print(dataDisplay)

condition = True
while condition == True:
    for data in AllData:
        print(data.replace("))
    choice = input("1. New Staff\n2. Delete Staff\n3. View Summary Data\n4. Save & Exit\nInput Choice: ")
    if choice == '1':
        print("New Staff")
        conditionID = False
        conditionName = False
        conditionPos = False
        conditionSal = False
        
        while conditionID == False:
            ID = input("Input ID [SXXXX]:")
            if len(ID) != 5 or ID[0] != 'S' or (ID[1::].isdigit()) == False or ID in dataList:
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
            Position = input("Input Position[Staff|Officer|Manager]:")
            if Position not in ["Manager","Staff","Officer"]:
                pass
            else:
                toAddPosition = Position
                conditionPos = True
        
        
        while conditionSal == False:
            Salary = input("Input Salary for {}".format(toAddPosition))
            if toAddPosition == 'Manager' and int(Salary) > 10000000:
                toAddSalary = Salary
                conditionSal = True
            elif toAddPosition == 'Staff' and 3500000 < int(Salary) < 7000000:
                toAddSalary = Salary
                conditionSal = True
            elif toAddPosition == 'Officer' and 7000001 < int(Salary) < 10000000:
                toAddSalary = Salary
                conditionSal = True
        AllData.append("{}#{}#{}#{}".format(toAddID,toAddName,toAddPosition,toAddSalary))
    ###########        
    elif choice == '2':
        print("Delete Staff")
        toDeleteID = input("InputID[SXXXX]:")
        
        for data in dataList:
            if toDeleteID in data:
                dataList.remove(data)
                print("Data has been successfully deleted")
                break
            else:
                print("Not Found")
                
    #################   
    elif choice == '3':
        print("1. Staff\nMinimum Salary: 4500000\nMaximum Salary: 5000000\nAverage Salary: 4750000\n")
        print("2. Officer\nMinimum Salary: 8500000\nMaximum Salary: 8500000\nAverage Salary: 8500000\n")
        print("3. Manager\nMinimum Salary: 10700000\nMaximum Salary: 10700000\nAverage Salary: 10700000\n ")
        
    elif choice == '4':
        print("Save and Exit")
        with open(filename) as file:
            for data in dataList:
                file.write(data)
            condition = False
        
    
    
    
    
    
    
    
    

    




#%%
