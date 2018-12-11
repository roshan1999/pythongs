from task1 import ATM
def main():
	initial = int(input("Enter initial amount of account"))
	minbal=int(input("Enter minimum balance of account"))	
	atm_1= ATM(initial,minbal)
	amt = int(input("Enter amount to withdraw"))
	atm_1.withdraw(amt)
	depamt = int(input("Enter amount to deposit"))
	atm_1.deposit(depamt)
	print("balance = ",atm_1.balance,"\n minimum = ",atm_1.min_bal)
if __name__ == '__main__':
	main()
