class Bankaccount:
    def __init__(self,int_rate, balance): #parameters
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        
        self.balance += amount
        print("\n Deposited:", amount)
    
    def withdraw(self, amount):
        # amount = float(input())
        if self.balance >= amount:
            self.balance -= amount
            print("\n Withdrew:", amount)
        else:
            print("\n You're Broke  ")
    
    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
    

    def yield_interest(self):
        self.balance += self.balance * self.int_rate 
        
        

George = Bankaccount(0.03, 100)
George.deposit(10.0) 
George.deposit(25.0) 
George.deposit(50.0) 
George.withdraw(10.0) 
George.yield_interest()
George.display_account_info()

Phil = Bankaccount(0.03, 1000)
Phil.deposit(25.0) 
Phil.deposit(15.0) 
Phil.withdraw(900.0) 
Phil.yield_interest()
Phil.display_account_info()




