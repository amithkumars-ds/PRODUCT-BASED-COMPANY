class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be less than 0!")
        self._balance = value



if __name__ == "__main__":
    account = BankAccount(1000)

    print(account.balance)  # 1000

    account.balance = 2000
    print(account.balance)  # 2000

    try:
        account.balance = -500
    except ValueError as e:
        print(e)
