class bank:
    # class variable
    bank_name = "State bank of india"
    
    def __init__(self,name,ac_no,ifsc,balance,count=0,option="none",amount=0):
        self.name = name
        self.ac_no = ac_no
        self.ifsc = ifsc
        self.balance = balance
        self.count=count
        self.option=option
        self.amount=amount
        self.l1=[]
        
    def widthdraw(self,amount):
        if amount>self.balance:
            print("incuificient Balance!!!")
            print("your current balance is :",self.balance) 
            
        else:
            self.balance = self.balance-amount
            print("withdraw successfuly")
            print("your current balance is :",self.balance)
            self.count+=1
            self.option = "withdraw"
            self.amount = amount
            self.l1.append((self.count,self.option,self.amount))
            
            
    def deposit(self,amount):
        if amount>=5000:
            self.balance+=amount
            print("deposit successfuly")
            print("your current balance is :",self.balance)
            self.count+=1
            self.option = "deposit"
            self.amount = amount
            self.l1.append((self.count,self.option,self.amount))
            
        
        else:
            print("min deposite 5000")
            
    def history(self):
        # 1 withdraw 5000
        print("trasection history ")
        # print(f"{self.l1}")
        f1 = open("history.txt","a")
        f1.write("\ntrasection history")
        for i in self.l1:
            i="\n"+str(i)
            f1.write(str(i))
            
        f1.close()
            
    def mini_statement(self):
        print("name : ",self.name)
        print("ac no : ",self.ac_no)
        print("ifsc : ",self.ifsc)
        print("balance : ",self.balance)
        
ac1 = bank("devarsh",12345678,"sbin001",120000)
print(ac1.bank_name)
print(bank.bank_name)
print("-"*50)        
ac1.mini_statement()
ac1.deposit(3000)
ac1.deposit(30000)
ac1.widthdraw(20000000)
ac1.widthdraw(30000)
print("-"*50)

ac2 = bank("manthan",000000,"sbin001",120000)
ac2.widthdraw(6000)
ac2.deposit(6000)
ac2.deposit(6000)
ac2.widthdraw(10000)
print(ac2.count)
ac2.history()
