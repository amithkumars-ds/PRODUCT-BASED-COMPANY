# Polymorphism means the same interface can produce different behavior depending on the object.

class Payment:
    def pay(self, amount):
        return f"Processing generic payment of {amount}"


class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"


class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using UPI"


if __name__ == "__main__":
    payments = [
        CreditCardPayment(),
        UPIPayment(),
        Payment()
    ]

    for payment in payments:
        print(payment.pay(1000))
