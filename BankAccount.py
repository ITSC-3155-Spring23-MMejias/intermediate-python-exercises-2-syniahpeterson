# Syniah Peterson

class BankAccount:
    def __init__(self, account_name, starting_balance:int, amount1, amount2):
        self.account_name = account_name
        self.starting_balance = starting_balance
        self.amount1 = amount1
        self.amount2 = amount2
    
    def deposit(self):
        self.balance = self.starting_balance + self.amount1
        return self.balance

    def withdraw(self):
        self.balance = self.balance - self.amount2
        return self.balance

    def get_balance(self):
        print(f'{self.account_name} has a balance of ${self.balance}')