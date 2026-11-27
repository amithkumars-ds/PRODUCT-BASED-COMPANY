# Exception Handling Block
# ---------------------------------------------------
# try   	Executes the risky code
# except 	Executes when a matching exception occurs
# else  	Executes only when no exception occurs
# finally 	Executes regardless of success or failure

def process_payment(amount, balance):
    if amount > balance:
        raise ValueError("Balance lower than amount!")
    return balance - amount


try:
    new_balance = process_payment(1000, 5000)
    print("Remaining balance: {0}".format(new_balance))

except TypeError as e:
    print(f"One of the values is not a number!: {e}")

else:
    print("Payment processing completed")


