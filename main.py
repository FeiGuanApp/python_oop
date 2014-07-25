from CheckingModel import Checking 

def main():
	check1 = Checking("1234", 500, 0.50)
	print(check1)
	check1.withdraw(100)
	print(check1)
	check1.deposit(200)
	print(check1)

if __name__ == '__main__':
	main()