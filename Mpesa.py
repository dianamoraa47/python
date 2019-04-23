class mpesa:
	 def __init__(self,name,balance,withdraw,deposit):
         self.name = name
         self.balance = balance
         self.withdraw = withdraw
         self.deposit = deposit



    def deposit(self,amount):
    	deposit = amount + self.balance
    	self.balance = self.balance+amount
    	message1="confirmed you have deposited{},your current balance is Ksh{}".format(self.name,amount,self.balance)
    	print(message1)

    def withdraw(self,amount):
    	deposit = self.balance-amount
    	message2="confirmed you have withdrawn{},your current balance is Ksh{}".format(self.name,amount,self.balance)
    	print(message2)

    def check_balance(self):
        check_balance = balance
        message3="confirmed you have withdrawn{},your current balance is Ksh{}".format(self.name,amount,self.balance)
    	print( message3)
    	 