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

        self.transaction_history = [] 

    def record_transaction(self, transaction: dict):
        if not isinstance(transaction, dict):
            raise TypeError("Transaction must be a dictionary")

        required_fields = {
            "transaction_type",
            "amount",
            "balance_after_transaction"
        }

        if set(transaction.keys()) != required_fields:
            raise ValueError("Invalid transaction structure")

        if transaction["transaction_type"] not in ("deposit", "withdrawal"):
            raise ValueError("Invalid transaction type")

        if not isinstance(transaction["amount"], (int, float)) or isinstance(transaction["amount"], bool) or transaction["amount"] <= 0:
            raise ValueError("Invalid transaction amount")

        self.transaction_history.append(transaction.copy())

    def get_transaction_history(self):
        if self.transaction_history:
            print("TRANSACTION DETAILS")
            print("-"*80)

            for transaction in self.transaction_history:
                print(transaction, "\n")
        else:
            print("No Transactions Found!!")

        return [transaction.copy() for transaction in self.transaction_history]

    
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
        
        transaction = {
                "transaction_type": "deposit",
                "amount": amount,
                "balance_after_transaction": self.__balance
                }

        self.record_transaction(transaction)

        return f"Deposit of {amount} successful, Balance: {self.__balance}"

    def _validate_balance(self, amount):
        final_balance = self.__balance - amount
        if final_balance < self.minimum_balance:
            raise ValueError("Amount Exceeds Minimum Balance! Try lower amount.")

    def withdraw(self, amount):
        self._validate_amount(amount)
        self._validate_balance(amount)
        self.__balance -= amount

        transaction = {
                "transaction_type": "withdrawal",
                "amount": amount,
                "balance_after_transaction": self.__balance
                }

        self.record_transaction(transaction)

        return f"Withdrawl of {amount} successful, Balance: {self.__balance}"   






if __name__ == "__main__":

    account1 = BankAccount("Kumar", 2000)
    account2 = BankAccount("Rahul", 5000)

    # TEST 1: Independent transaction histories
    account1.deposit(1000)
    account2.withdraw(500)

    print("\nTEST 1: Independent histories")
    print("Account 1:", account1.get_transaction_history())
    print("Account 2:", account2.get_transaction_history())

    # TEST 2: Failed transactions must not affect history
    print("\nTEST 2: Failed transactions")
    history_before = account1.get_transaction_history()

    try:
        account1.deposit(-500)
    except ValueError as e:
        print("Caught:", e)

    try:
        account1.withdraw(100000)
    except ValueError as e:
        print("Caught:", e)

    assert account1.get_transaction_history() == history_before
    print("PASS: Failed transactions did not modify history")

    # TEST 3: Empty transaction history
    print("\nTEST 3: Empty history")
    account3 = BankAccount("Priya", 1000)

    assert account3.get_transaction_history() == []
    print("PASS: New account has empty history")

    # TEST 4: External modification isolation
    print("\nTEST 4: History isolation")
    history = account1.get_transaction_history()
    history.clear()

    assert len(account1.get_transaction_history()) == 1
    print("PASS: Clearing returned list did not affect original")

    # TEST 5: Transaction schema validation
    print("\nTEST 5: Invalid transaction records")

    invalid_transactions = [
        {"amount": 500},
        {"transaction_type": "transfer", "amount": 500,
         "balance_after_transaction": 1000},
        {"transaction_type": "deposit", "amount": -500,
         "balance_after_transaction": 1000},
        {"transaction_type": "deposit", "amount": True,
         "balance_after_transaction": 1000},
        {"transaction_type": "deposit", "amount": 500,
         "balance_after_transaction": 1000, "extra": "field"}
    ]

    for transaction in invalid_transactions:
        try:
            account1.record_transaction(transaction)
            print("FAIL:", transaction)
        except (ValueError, TypeError) as e:
            print("PASS:", e)

    # TEST 6: Exact minimum balance
    print("\nTEST 6: Minimum balance")
    account4 = BankAccount("Arun", 1000)

    print(account4.withdraw(500))
    assert account4._get_balance() == "Balance: 500"
    print("PASS: Minimum balance maintained")

    print("\nALL TESTS COMPLETED")

