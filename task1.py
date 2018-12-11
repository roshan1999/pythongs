import numpy as np
def check_per_sqr(num):
	fact =0
	count = num-1
	while (count >=1):
		if(num%count == 0):
			fact+=count
		count=count-1
	if(fact == num):
		return True
	elif (fact==0):
		return False
	else:
		return False

def main():
	x = np.random.randint(1,101,size = 20)
	perflist=x.tolist()
	perflist = list(filter(lambda x:(check_per_sqr(x)),perflist))
	if perflist:
		print(perflist)
	else:
		print("List is empty")
class ATM:
	balance = 0
	min_bal = 0
	def __init__(self,og,min_bal):
		self.balance+=og
		self.min_bal=min_bal
		print('Balance updated to ',self.balance)
	def withdraw(self,amount):
		if(self.balance-amount<self.min_bal):
			print('Withdraw terminated, Minimum Balance: ',self.min_bal,' not achieved')
		else:
			self.balance-=amount
			print('Balance updated to: ',self.balance)
	def deposit(self,amount):
		self.balance+=amount;
		print('Balance updated to: ',self.balance)


if __name__ == '__main__':
	str = input('Enter 1 for perfect number program and 3 for exception program')
	if(str=="1"):
		main()
	else:
		i=2;
		while(i>0):
			try:
				print("Iteration number = ",3-i)
				i= i-1
				print("ans = ",1/i)
				print("First error would be name error as x(global) not defined: ")
				print("but this would raise name error",x)
			except ZeroDivisionError as err:
				print('Zero division error')
			except NameError:
				print('Name error variable not defined')
