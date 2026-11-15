from decimal import Decimal

class BankAccount:
    def __init__(self,
                 account_holder: str,
                 balance: Decimal):
        self.account_holder = account_holder

        if balance < 0:
            raise ValueError("Balance cannot be less than zero!")
        self.__balance = balance

    def get_balance(self) -> Decimal:
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Enter valid amount!")
        self.__balance += amount

    def _validate_withdrawal(self, amount):
        if self.__balance - amount < 0:
            raise ValueError("Balance cannot be less than zero!")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Enter valid amount!")
        self._validate_withdrawal(amount)
        self.__balance -= amount







if __name__ == "__main__":

    # Create bank account
    account = BankAccount("Kumar", Decimal("10000.00"))

    # Check initial balance
    print("Initial Balance:", account.get_balance())

    # Deposit money
    account.deposit(Decimal("2500.00"))
    print("After Deposit:", account.get_balance())

    # Withdraw money
    account.withdraw(Decimal("1500.00"))
    print("After Withdrawal:", account.get_balance())

    # Test invalid deposit
    try:
        account.deposit(Decimal("-500.00"))
    except ValueError as e:
        print("Deposit Error:", e)

    # Test invalid withdrawal
    try:
        account.withdraw(Decimal("-200.00"))
    except ValueError as e:
        print("Withdrawal Error:", e)

    # Test insufficient balance
    try:
        account.withdraw(Decimal("50000.00"))
    except ValueError as e:
        print("Insufficient Balance Error:", e)

    # Verify balance remains unchanged after failed transactions
    print("Final Balance:", account.get_balance())
