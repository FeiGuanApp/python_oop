import unittest
from CheckingModel import Checking 

class TestWithdrawAndDeposit(unittest.TestCase):
	def setUp(self):
		self.checking = Checking("1234", 500, 0.50)

	def test_withdraw(self):
		self.checking.withdraw(100)
		self.assertEqual(self.checking.balance, 399.5)

	def test_deposit(self):
		self.checking.deposit(50)
		self.assertEqual(self.checking.balance, 550)

	def test_withdraw2(self):
		self.checking.withdraw(200)
		self.assertEqual(self.checking.balance, 299.5)

	def test_withdraw3(self):
		self.checking.withdraw(600)
		self.assertEqual(self.checking.balance, 500)

if __name__ == '__main__':
    unittest.main()