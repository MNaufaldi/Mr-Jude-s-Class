#%%
import json
filename = "Bank.json"

def load_file():
    global stonks
    with open(filename) as f:
        stonks = json.load(f)
class Account:
    __balance = 0
    
    def __init__(self,balance):
        self.__balance = balance
    def getBalance(self):
        return self.__balance
    def deposit(self,value):
        if 0 < value:
            self.__balance = self.__balance + value
            return True
        else:
            return False
    def withdraw(self,value):
        if value <= self.__balance and value > 0:
            self.__balance = self.__balance - value
            return True
        else:
            return False

class Customer:
    __firstName = str
    __lastName = str
    __Account = Account(50)
    
    def __init__(self,fname,lname):
        self.__firstName = fname
        self.__lastName = lname
    def getFirstName(self):
        return self.__firstName
    def getLastName(self):
        return self.__lastName
    def getAccount(self):
        return self.__Account.getBalance()
    def setAccount(self,Account):
        self.__Account = Account
    def createOnApp(self):
        self.__Username = input("Username: ")
        self.__Password = input("Password: ")
        
class Bank:
    __customers = []
    __numberOfCustomers = 0
    __bankName = ""

    def __init__(self,bName):
        self.__bankName = bName
    def addCustomer(self,fname,lname):
        name = fname +" "+ lname
        self.__customers.append(name)
    def getNumOfCustomers(self):
        __numberofCustomers = len(self.__customers)
        return __numberofCustomers
    def getCustomer(self,index):
        return self.__customers[index]   

def new():#Update new account to json file with 5k in balance
    global Balance,stonks
    Balance = Customer1.getAccount()
    stonks['Banks'][BankName][username] = {
            'First Name':FName,
            'Last Name':LName,
            'Account':{'Account Name':'Name','Balance':Balance,'Password':Password}}
    updateJson()
    
def update():#Update the balance in account and 'Balance' variable
    global Balance,stonks
    stonks['Banks'][BankName][username]['Account']['Balance'] = Customer1.getAccount()
    Balance = Customer1.getAccount()
    
def updateJson():#Update everything that changed to Json
    with open(filename,'w+') as w:
        global stonks,BankName,username,Password,FName,LName,Balance
        stonks['Banks'][BankName][username] = {'First Name':FName,'Last Name':LName,'Account':{'Account Name':'Name','Balance':int(Balance),'Password':Password}}
        data = stonks
        
        json.dump(data,w,indent=4)
        

        
        

#Load data phase
#It gets all the customers in a list??
load_file()
Banks = []
Customers = []
BankName = ''

#Find bank phase
#It needs the bank name and it will store the bank name
for bank in stonks['Banks']:
    Banks.append(bank)
for index in range                              (len(Banks)):
    print(str(index + 1)+".",Banks[index])
BankName = int(input("Which Bank? "))
BankName = Banks[BankName-1]
 
for data in stonks['Banks'][BankName]:
    Customers.append(data)
choice = input("1. Login\n2. Create a new account\nWhat do you want to do? ")

#For User
if choice == "1":    
    #Login phase
    #Banks are already chosen
    BankName = "Bank name"#input choices of bank thats in there
    BankIndex = 0#Auto find the bank index
    CustIndex = 0#Auto find the cust index after login
    username = 'Customers username'#input("Please input your username: ")
    password = 'Test'#input("Please input your password: ")
    #Check login phase and assigning the account
    for customer in stonks:#Checking for every customers
        if username in Customers:#Assigning account data to variables so it will be easier to call
            if password == stonks['Banks'][BankName][username]['Account']['Password']:
                FName = stonks['Banks'][BankName][username]['First Name']
                LName = stonks['Banks'][BankName][username]['Last Name']
                AccountName = stonks['Banks'][BankName][username]['Account']['Account Name']
                Balance = stonks['Banks'][BankName][username]['Account']['Balance']
                Password = stonks['Banks'][BankName][username]['Account']['Password']
                print("Login Successful")
            else:
                print("Invalid Username or Password")
        else:
            print("Invalid Username or Password")
            
    #Setting up the account the classes
    Customer1 = Customer(FName,LName)
    Account1 = Account(int(Balance))
    Customer1.setAccount(Account(int(Balance)))
    Customer1.getAccount()
    
    #Display Logged in
    choice = 0
    while choice != '3':  
        print("Welcome",FName,LName,"what do you want to do?")
        print("1. Deposit\n2. Withdraw\n3. Exit")
        choice = input("?")
        
        if choice == '1':
            #Another display and choice
            print("Your balance is: ",Customer1.getAccount())
            howmuch = int(input("How much do you want to deposit? "))
            if howmuch > 0:
                Account1.deposit(howmuch)
                Customer1.setAccount(Account1)
                print("Your balance now is: ",Customer1.getAccount())
                update()
            else:
                print("Invalid number")
        elif choice == '2':
            print("Your balance is: ",Customer1.getAccount())
            howmuch = int(input("How much do you want to withdraw? "))
            if 0 < howmuch < Customer1.getAccount():
                Account1.withdraw(howmuch)
                Customer1.setAccount(Account1)
                print("Your balance now is: ",Customer1.getAccount())
                update()
            else:
                print("Invalid number")
        elif choice == '3':
            updateJson()
            break
        
#For creating new account purposes
elif choice == "2":
    FName = input("First name: ")
    LName = input("Last name: ")
    username = input("Username: ")
    Password = input("Password: ")
    if username in Customers:
        print("Username already existed")
        FName,LName,username,Password = "","","",""
    else:
        Account1 = Account(5000)
        Customer1 = Customer(FName,LName)
        Customer1.setAccount(Account1)
        new()


#%%