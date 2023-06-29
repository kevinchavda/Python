class Bank:

    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello",self.cname,",Your Account Number",self.acno," Is Open With ",self.balance," Rs.")
    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("Sorry insufficient Fund")
    def checkBalance(self):
        print ("Current Balance : ",self.balance)
b1=Bank()
b1.openAccount(555,"Kevin",3223)
b1.deposit(5000)
b1.checkBalance()
b1.withdraw(4000)
b1.checkBalance()

