class Staff:
    def __init__(self,ID,name,position,salary):
        self.ID = ID
        self.name = name
        self.position = position
        self.salary = salary
        
    def getID(self):
        return self.ID
    def getName(self):
        return self.name
    def getPosition(self):
        return self.position
    def getSalary(self):
        return self.salary
    
    def setID(self,ID):
        self.ID = ID
    def setName(self,name):
        self.name = name
    def setPosition(self,position):
        self.position = position
    def setSalary(self,salary):
        self.salary = salary
        
class Position:
    def __init__(self,name,minsalary,maxsalary):
        self.name = name
        self.minsalary = minsalary
        self.maxsalary = maxsaslary
    
    
    
    