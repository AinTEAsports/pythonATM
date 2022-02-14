import sys


# Creating class
class BankAccount:
	
	def __init__(self, name):
		self.name = name
		self.accountValue = 100

	
	def deposer(self, montant):
		self.accountValue += montant
	

	def retirer(self, montant):
		if self.accountValue - montant >= 0:
			self.accountValue -= montant
			return
		print(f"You don't enough money to retire {montant}€")


	def getAccountValue(self):
		return self.accountValue


	def getAccountName(self):
		return self.name


# I define my account
myAccount = BankAccount("AinTEAsports")


menuChoice = """
0- Quitter
1- Retirer
2- Deposer
3- Afficher solde
4- Afficher 5 dernieres operations
5- Afficher retraits
6- Afficher depots
"""

print(f"Welcome to your Bank {myAccount.getAccountName()} !")


continuer = True
while continuer:
	print(menuChoice)
	userChoice = input("Enter your choice : ")

	while userChoice not in [str(i) for i in range(7)]:
		print("\nEnter a valid option !\n")
		userChoice = input("Enter your choice : ")
	
	if userChoice == "0":
		print(f"\nGoodbye {myAccount.getAccountName()} !")
		sys.exit()
	elif userChoice == "1":
		toRetire = input("Enter how much money you want to retire : ")
		if toRetire.isdigit():
			myAccount.retirer(toRetire)
		else:
			print("Merci d'entrer un chiffre\n")
	elif userChoice == "2":
		toDepose = input("Enter how much do you want to depose : ")
		if toDepose.isdigit():
			myAccount.deposer(toDepose)
		else:
			print("Merci d'entrer un chiffre\n")
	elif userChoice == "3":
		print(myAccount.getAccountValue())
	elif userChoice == "4":
		pass
	elif userChoice == "5":
		pass
	elif userChoice == "6":
		pass
	else:
		print("\n!!!ERROR !!!\n")

	wantContinue = input("Do you want to continue ? [Y/n] : ").lower()
 
	if wantContinue == 'y':
		continuer = False
