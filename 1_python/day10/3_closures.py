def create_account(initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance

        if amount <= 0:
            raise ValueError("Invalid Deposit Amount!")
        
        balance += amount
        return balance

    return deposit 


account = create_account(1000)
print(account(500))

