import random
import time

random.seed(time.time())

class Account(object):
	
	accountNumber = 0
	accountHolder = ""
	cash = 0

	def __init__(self, holder, startingCash):
		self.accountHolder = holder
		self.cash = float(startingCash)
		self.accountNumber = random.randint(0, 9999)

	def Display(self):
		print("Account Number {}".format(self.accountNumber))
		print("Account Holder {}".format(self.accountHolder))
		print("Account Cash   {}".format(self.cash))

bankAccounts = []

while True:
	command = int(raw_input("Hello, would you like to create an account (1) or access an account (2)? "))
	if command == 1:
		name = raw_input("What is your name? ")
		startingCash = raw_input("How much money would you like to deposit? ")

		newAccount = Account(name, startingCash)
		bankAccounts.append(newAccount)

		print("Your account has been made, please remember your number")
		newAccount.Display()
	elif command == 2:
		number = int(raw_input("What is your account ID? "))
		for account in bankAccounts:
			if account.accountNumber == number:
				print("Found Your Account")
				account.Display()

				action = int(raw_input("Deposit (1) or Withdraw (2)? "))
				amount = int(raw_input("How much? "))

				if action == 1:
					account.cash += amount
				elif action == 2:
					account.cash -= amount

				print("Thanks, action completed, here is your account now: ")
				account.Display()
