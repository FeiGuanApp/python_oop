class Account:

	accountNumber = ""
	balance = 0

	def __init__(self, accountNumber, balance):
		self.accountNumber = accountNumber
		self.balance = balance
    
	def __str__(self):
		return "Account number: " + accountNumber + "\nBalance: balance\n"
    