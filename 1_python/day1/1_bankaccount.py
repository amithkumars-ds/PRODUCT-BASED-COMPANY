class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print(f"Balance: {self.balance}")


    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount} to account successfully!")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"Withdrawn {amount} from account!")


        
if __name__ == "__main__":
    account = BankAccount("Kumar", 1000)
    account.deposit(500)
    account.withdraw(200)

    account2 = BankAccount("Harsha", 2000)
    account2.display_balance()
    account2.withdraw(500)

    # displaying balances
    account.display_balance()
    account2.display_balance()
