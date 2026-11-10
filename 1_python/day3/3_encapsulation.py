class BankAccount:
    def __init__(self,
                 account_holder: str,
                 initial_balance: int):
        self.account_holder = account_holder # public attribute
        if initial_balance <= 0:
            raise ValueError("Amount cannot be zero or Negative!")
        self.__balance = initial_balance # private attribute


    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount cannot be zero or Negative!")

        self.__balance += amount


    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount cannot be zero or Negative!")
        if amount > self.__balance:
            raise ValueError("Insufficient Balance!")
        self.__balance -= amount


    def get_balance(self):
        return f"Balance: {self.__balance}"








if __name__ == "__main__":
    account = BankAccount("Kumar", 1000)
    print(account._BankAccount__balance)

    print("Initial balance:", account.get_balance())

    account.deposit(500)
    print("After deposit:", account.get_balance())

    account.withdraw(200)
    print("After withdrawal:", account.get_balance())

    try:
        account.deposit(-100)
    except ValueError as e:
        print("Invalid deposit:", e)

    print("After invalid deposit:", account.get_balance())

    try:
        account.withdraw(2000)
    except ValueError as e:
        print("Withdrawal failed:", e)

    print("After insufficient balance withdrawal:", account.get_balance())

    account.withdraw(-50)
    print("After invalid withdrawal:", account.get_balance())

    print("Account holder:", account.account_holder)

    # Test encapsulation
    print(account.__balance)
