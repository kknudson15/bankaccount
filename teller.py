from bankaccount import *

bank1 = BankAccount('Kyle', 1000)
new_account_holder = False
quit = False

print("Hi Welcome to the bank:")
while quit == False:
    visit_reason = input("""What would you like to do today
        1.Open an account
        2.Deposit Money
        3.Withdraw Money
        4.All done for the day
        """)

    if visit_reason == '1' or 'open' in visit_reason.lower():
        owner = input("Who will be the owner of the account?")
        amount = float(input("How much would you like to deposit into the account intially"))
        bank2 = BankAccount(owner, amount)
        new_account_holder == True
    elif visit_reason == '2' or 'deposit' in visit_reason.lower():
        amount = float(input("How much money do you want to deposit into your account?"))
        if new_account_holder == False:
            bank1.deposit(amount)
        else:
            bank2.deposit(amount)
    elif visit_reason == '3' or 'withdraw' in visit_reason.lower():
        amount = float(input('How much money do you want to withdraw?'))
        if new_account_holder == False:
            bank1.withdraw(amount)
        else:
            bank2.withdraw(amount)
    elif visit_reason == '4' or 'all' in visit_reason.lower():
        print("Thank you for banking with us, Please come again!")
        quit = True
    else:
        print('Invalid input!')