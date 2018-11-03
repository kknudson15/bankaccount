class BankAccount:
    def __init__(self,owner, balance):
        self.owner = owner 
        self.balance = balance

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("FUNDS UNAVAILABLE!")
        else:
            self.balance -= amount
            print(f'The current balance is now: {self.balance}')
    def deposit(self, amount):
        self.balance += amount
        print(f'The current balance is now: {self.balance}')

    def __str__(self):
        return (f'Owner: {self.owner}\nBalance: {self.balance}')