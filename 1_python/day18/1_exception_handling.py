class InsufficientBalanceError(Exception):
    pass


def process_payment(amount, balance):
    if amount > balance:
        raise InsufficientBalanceError(
            f"Requested: {amount}, Available: {balance}"
        )

    return balance - amount

try:
    new_balance = process_payment(10000, 5000)

except InsufficientBalanceError as e:
    print(f"Insufficient balance! {e}")

except TypeError as e:
    print(f"Invalid data type: {e}")

except ValueError as e:
    print(f"Payment rejected: {e}")

else:
    print(f"Payment successful, Balance: {new_balance}")

finally:
    print("Payment processing completed")
