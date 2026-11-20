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

    def _validate_transaction(self, transaction: dict):
        if not isinstance(transaction, dict):
            raise TypeError("Transaction must be a dictionary")

        schemas = {
            "deposit": {"transaction_type", "amount", "balance_after_transaction"},
            "withdrawal": {"transaction_type", "amount", "balance_after_transaction"},
            "transfer_in": {"transaction_type", "amount", "balance_after_transaction", "sender_bank_account"},
            "transfer_out": {"transaction_type", "amount", "balance_after_transaction", "receiver_bank_account"}
        }

        transaction_type = transaction.get("transaction_type")

        if transaction_type not in schemas:
            raise ValueError("Invalid transaction type")

        if set(transaction.keys()) != schemas[transaction_type]:
            raise ValueError("Invalid transaction structure")

        amount = transaction["amount"]

        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            raise ValueError("Invalid transaction amount")

    def record_transaction(self, transaction: dict):
        self._validate_transaction(transaction)
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

    def transfer_to(self, receiver: "BankAccount", amount):
        # Step 1: Validate receiver
        if not isinstance(receiver, BankAccount):
            raise TypeError("Receiver must be a BankAccount")

        if receiver is self:
            raise ValueError("Cannot transfer to the same account")

        # Step 2: Validate amount and sender balance
        self._validate_amount(amount)
        self._validate_balance(amount)

        # Step 3: Calculate balances without modifying them
        sender_new_balance = self.__balance - amount
        receiver_new_balance = receiver.__balance + amount

        # Step 4: Prepare transaction records
        sender_transaction = {
            "transaction_type": "transfer_out",
            "amount": amount,
            "balance_after_transaction": sender_new_balance,
            "receiver_bank_account": receiver.account_number
        }

        receiver_transaction = {
            "transaction_type": "transfer_in",
            "amount": amount,
            "balance_after_transaction": receiver_new_balance,
            "sender_bank_account": self.account_number
        }

        # Step 5: Validate both records before changing balances
        self._validate_transaction(sender_transaction)
        receiver._validate_transaction(receiver_transaction)

        # Step 6: Commit changes
        self.__balance = sender_new_balance
        receiver.__balance = receiver_new_balance

        self.record_transaction(sender_transaction)
        receiver.record_transaction(receiver_transaction)

        return f"Transfer of {amount} successful"






if __name__ == "__main__":

    sender = BankAccount("Kumar", 5000)
    receiver = BankAccount("Rahul", 2000)

    # TEST 1: Successful transfer
    print("\nTEST 1: Successful transfer")

    print(sender.transfer_to(receiver, 1000))

    assert sender._get_balance() == "Balance: 4000"
    assert receiver._get_balance() == "Balance: 3000"

    print("PASS: Both balances updated correctly")

    # TEST 2: Transaction histories
    print("\nTEST 2: Transaction histories")

    sender_history = sender.get_transaction_history()
    receiver_history = receiver.get_transaction_history()

    assert sender_history[-1]["transaction_type"] == "transfer_out"
    assert receiver_history[-1]["transaction_type"] == "transfer_in"

    print("PASS: Both transaction histories updated")

    # TEST 3: Insufficient balance
    print("\nTEST 3: Insufficient balance")

    sender_balance_before = sender._get_balance()
    receiver_balance_before = receiver._get_balance()

    sender_history_before = sender.get_transaction_history()
    receiver_history_before = receiver.get_transaction_history()

    try:
        sender.transfer_to(receiver, 10000)
    except ValueError as e:
        print("Caught:", e)

    assert sender._get_balance() == sender_balance_before
    assert receiver._get_balance() == receiver_balance_before
    assert sender.get_transaction_history() == sender_history_before
    assert receiver.get_transaction_history() == receiver_history_before

    print("PASS: Failed transfer changed nothing")

    # TEST 4: Invalid amount
    print("\nTEST 4: Invalid amount")

    try:
        sender.transfer_to(receiver, -500)
    except ValueError as e:
        print("Caught:", e)

    # TEST 5: Invalid receiver
    print("\nTEST 5: Invalid receiver")

    try:
        sender.transfer_to("Not an account", 500)
    except TypeError as e:
        print("Caught:", e)

    # TEST 6: Transfer to same account
    print("\nTEST 6: Same account transfer")

    try:
        sender.transfer_to(sender, 500)
    except ValueError as e:
        print("Caught:", e)

    # TEST 7: Minimum balance boundary
    print("\nTEST 7: Minimum balance")

    account3 = BankAccount("Priya", 1000)
    account4 = BankAccount("Arun", 1000)

    account3.transfer_to(account4, 500)

    assert account3._get_balance() == "Balance: 500"
    assert account4._get_balance() == "Balance: 1500"

    print("PASS: Minimum balance maintained")

    print("\nALL TESTS COMPLETED")

