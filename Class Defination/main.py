# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Account:

    def __init__(self, accounttitle ,accountnumber,accountbalance):
        self.AccountTitle =accounttitle
        self.AccountNumber = accountnumber
        self.AccountBalance = accountbalance
    def getAccountTitle(self):
        return self.AccountTitle
    def getAccountNumber(self):
        return self.AccountNumber
    def getAccountBalance(self):
        return self.AccountBalance
    def setAccountTitle(self,actitle):
        self.AccountTitle= actitle
    def setAccountNumber(self,acno):
        self.AccountNumber = acno
    def setAccountBalance(self,acbal):
        self.AccountBalance = acbal
    def Deposit(self,amount):
        #self.AccountBalance = self.AccountBalance + amount
        self.AccountBalance += amount;
    def WithDraw(self,amount):
        self.AccountBalance -= amount;

    def AccountSumary(self):
        print("Account Title :" + self.AccountTitle)
        print("Account Number :"  + str(self.AccountNumber))
        print("Account Balance :" + str(self.AccountBalance))

if __name__ == '__main__':
    ac = Account("Muhammad Ahmed Khan",1330300303,3500.56)
    ac.AccountSumary()
    ac.Deposit(1500)
    ac.AccountSumary()
    ac.WithDraw(1000)
    ac.AccountSumary()