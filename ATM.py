import sys
import termcolor


asciiText = """
  _______             __    _______             
 |   _   .---.-.-----|  |--|       .-----.---.-.
 |.  1   |  _  |     |    <|.|   | |  -__|  _  |
 |.  _   |___._|__|__|__|__`-|.  |-|_____|___._|
 |:  1    \                  |:  |              
 |::.. .  /                  |::.|              
 `-------'                   `---'              
"""

asciiTextColored = termcolor.colored(asciiText, "red")


print(asciiTextColored)


# Creating class
class BankAccount:
	
	def __init__(self, name):
		self.name = name
		self.accountValue = 100
		self.operationNumber = 0

		# {"operationNumber" : operationValue}
		self.retraits = {}
		self.depots = {}

	def deposer(self, montant):
		self.accountValue += montant
		self.operationNumber += 1
		self.depots[str(self.operationNumber)] = montant


	def retirer(self, montant):
		if self.accountValue - montant >= 0:
			self.accountValue -= montant
			self.operationNumber += 1
			self.retraits[str(self.operationNumber)] = montant
			return

		print(f"You don't have enough money to retire {montant}€")


	def getAccountValue(self):
		return self.accountValue


	def getAccountName(self):
		return self.name


	def getDepots(self):
		return self.depots


	def getFiveLastOperations(self):
		fiveLastOperations = []
  
		if self.operationNumber == 0:
			return "Vous n'avez pas encore effectué d'opérations"
  
		if self.operationNumber <= 5:
			return list(self.retraits.values()) + list(self.depots.values())
  
		for i in range(self.operationNumber-4, self.operationNumber+1):
			if str(i) in self.retraits.keys():
				fiveLastOperations.append(self.retraits[str(i)])
			else:
				fiveLastOperations.append(self.depots[str(i)])
    
		return fiveLastOperations


	def getRetraits(self):
		return self.retraits


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
	
	if userChoice == "0":
		break
	elif userChoice == "1":
		toRetire = input("Enter how much money you want to retire : ")
		if toRetire.isdigit():
			myAccount.retirer(int(toRetire))
		else:
			print("\nMerci d'entrer un chiffre\n")
	elif userChoice == "2":
		toDepose = input("Enter how much do you want to depose : ")
		if toDepose.isdigit():
			myAccount.deposer(int(toDepose))
		else:
			print("\nMerci d'entrer un chiffre\n")
	elif userChoice == "3":
		print(myAccount.getAccountValue())
	elif userChoice == "4":
		print(myAccount.getFiveLastOperations())
	elif userChoice == "5":
		pass
	elif userChoice == "6":
		pass
	else:
		print("\nPlease enter a valid option !\n")


print(f"\nGoodbye {myAccount.getAccountName()} !")
