class BankAccount:
    account_counter = 0
    minimum_balance = 500

    def __init__(self, name, initial_balance):
        self.name = name
        if initial_balance < self.minimum_balance:
            raise ValueError("Minimum Balance is 500!")

        self.__balance = initial_balance
        BankAccount.account_counter += 1
        self.account_number = "KARB0"+str(BankAccount.account_counter)
    
    def _get_balance(self):
        return f"Balance: {self.__balance}"

    def display_info(self):
        balance = self._get_balance()
        return f"Account holder name: {self.name}" + balance
    
    @staticmethod
    def _validate_amount(amount):
        if amount <= 0:
            raise ValueError(f"Invalid Amount: {amount}")

    def deposit(self, amount):
        self._validate_amount(amount)
        self.__balance += amount
        
        return f"Deposit of {amount} successful, Balance: {self.__balance}"

    def _validate_balance(self, amount):
        final_balance = self.__balance - amount
        if final_balance < self.minimum_balance:
            raise ValueError("Amount Exceeds Minimum Balance! Try lower amount.")

    def withdraw(self, amount):
        self._validate_amount(amount)
        self._validate_balance(amount)
        self.__balance -= amount
        
        return f"Withdrawl of {amount} successful, Balance: {self.__balance}"




if __name__ == "__main__":

    # Create accounts
    account1 = BankAccount("Kumar", 2000)
    account2 = BankAccount("Rahul", 5000)
    account3 = BankAccount("Priya", 4000)

    print("=== Account Details ===")
    print(account1.display_info())
    print(account2.display_info())
    print(account3.display_info())

    print("\n=== Deposits ===")
    print(account1.deposit(2000))
    print(account2.deposit(5000))

    print("\n=== Withdrawals ===")
    print(account1.withdraw(500))
    print(account2.withdraw(1000))

    print("\n=== Invalid Transactions ===")
    print(account1.deposit(-500))
    print(account1.withdraw(100000))

    print("\n=== Final Account Details ===")
    print(account1.display_info())
    print(account2.display_info())

    print("\n=== Account Number Uniqueness ===")
    print(account1.account_number)
    print(account2.account_number)
    print(account3.account_number)

