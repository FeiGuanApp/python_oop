import AccountModel

class Checking(AccountModel.Account): 

  fee = 0


  def __init__(self, accountNumber, balance, fee):
    AccountModel.Account.__init__(self, accountNumber, balance)
    self.fee = fee
    
  def __str__(self):
    return "Account type: Checking\nAccount number: " + self.accountNumber + "\nBalance: " + str(self.balance) + "\n"
    
  def getFee(self):
    return  self.fee
    
  def deposit(self, amount):
    self.balance = self.balance + amount
    
  def withdraw(self, amount):
    if amount > self.balance:
      print "Insufficient funds!"
    else:
      self.balance = self.balance - self.fee - amount