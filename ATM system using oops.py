class atm:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
        
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("amount deposited",amount)
        else:
            print("invalid deposit amount")
            
    def withdraw(self,amount):
            if amount<=0:
                print("invalid amount")
                
            elif amount>self.__balance:
                print("insufficient balance")
            else:
                self.__balance-= amount
                print("amount withdrwal",amount)
                
    def check_balance(self):
            print("current balance",self.__balance)
            
            
atm=atm("rahul",0)

atm.deposit(1000)
atm.check_balance()
atm.deposit(5000)
atm.withdraw(7000)
atm.check_balance()
atm.withdraw(7000)


atm.check_balance()


                
        